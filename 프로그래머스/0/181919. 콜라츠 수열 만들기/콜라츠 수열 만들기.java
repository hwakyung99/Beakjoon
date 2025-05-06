import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        while(n > 1) {
            answer.add(n);
            n = n % 2 == 0 ? n / 2 : n * 3 + 1;
        }
        answer.add(1);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}