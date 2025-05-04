class Solution {
    public int solution(int a, int b) {
        String a_string = Integer.toString(a);
        String b_string = Integer.toString(b);
        
        int answer = Integer.max(Integer.parseInt(a_string + b_string), Integer.parseInt(b_string + a_string));
        
        return answer;
    }
}