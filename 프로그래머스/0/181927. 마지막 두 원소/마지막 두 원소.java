import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int length = num_list.length;
        int a = num_list[length - 1];
        int b = num_list[length - 2];
        
        int[] answer = Arrays.copyOf(num_list, length + 1);
        answer[length] = a > b ? a - b : a * 2;
        
        return answer;
    }
}