import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<Integer>();
        
        int i = 0, cnt = 0;
        
        while(i < progresses.length) {
            for(int j = i; j < progresses.length; j++) {
                progresses[j] += speeds[j];
            }

            while (i < progresses.length && progresses[i] >= 100) {
                cnt++;
                i++;
            }
            
            if(cnt > 0) {
                answer.add(cnt);
                cnt = 0;
            }
        }
        
        return answer.stream().mapToInt(k -> k).toArray();
    }
}