import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Group> map = new HashMap<>();
        
        for(int i = 0; i < genres.length; i++) {
            if(map.containsKey(genres[i])) {
                map.get(genres[i]).playSum += plays[i];
                map.get(genres[i]).songList.add(new Song(i, plays[i]));
            }
            else {
                map.put(genres[i], new Group(new Song(i, plays[i])));
            }
        }
        
        List<String> keySet = new ArrayList<>(map.keySet());
        keySet.sort((o1, o2) -> Integer.compare(map.get(o2).playSum, map.get(o1).playSum));
        
        List<Integer> answer = new ArrayList<>();
        for(String key : keySet) {
            int i = 0;
            while(!map.get(key).songList.isEmpty() && i < 2) {
                answer.add(map.get(key).songList.poll().index);
                i++;
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
    
    class Group {
        int playSum;
        PriorityQueue<Song> songList;
        
        public Group(Song song) {
            playSum = song.play;
            songList = new PriorityQueue<>();
            songList.add(song);
        }   
    }
    
    class Song implements Comparable<Song>{
        int index;
        int play;
        
        public Song(int index, int play) {
            this.index = index;
            this.play = play;
        }
        
        @Override
        public int compareTo(Song o) {
            if(this.play > o.play) {
                return -1;
            } else if(this.play == o.play) {
                return this.index > o.index ? 1 : -1;
            } else {
                return 1;
            }
        }
    }
}