import java.util.ArrayList;

class Solution {
    
    public int[] solution(int l, int r) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int i = l; i <= r; i++) {
            boolean flag = true;
            int tmp = i;
            while(tmp > 0) {
                if(tmp % 5 != 0) {
                    flag = false;
                    break;
                }
                tmp /= 10;
            }
            
            if(flag) answer.add(i);
        }
        
        if(answer.isEmpty()) answer.add(-1);
        return answer.stream().mapToInt(i -> i).toArray();
    }
}