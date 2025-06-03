import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Integer[] tmp = Arrays.stream(priorities).boxed().toArray(Integer[]::new);
        
        Arrays.sort(tmp, Collections.reverseOrder());
        
        int i = 0;
        while(i < priorities.length) {
            for(int j = 0; j < priorities.length; j++) {
                if(tmp[i] == priorities[j]){
                    answer++;
                    i++;
                    
                    if(j == location) return answer;
                }
            }
        }
        
        return answer;
    }
}