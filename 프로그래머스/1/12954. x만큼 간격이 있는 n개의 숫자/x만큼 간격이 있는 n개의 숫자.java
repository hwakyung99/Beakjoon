import java.util.*;

class Solution {
    public long[] solution(int x, int n) {
        List<Long> answer = new ArrayList<>();
        
        for(int i = 1; i < n + 1; i++) {
            answer.add((long)x * i);
        }
        
        return answer.stream().mapToLong(i -> i).toArray();
    }
}