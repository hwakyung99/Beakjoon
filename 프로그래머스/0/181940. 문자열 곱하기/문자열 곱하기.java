class Solution {
    public String solution(String my_string, int k) {
        StringBuilder answer = new StringBuilder(my_string);
        
        for(int i = 1; i < k; i++) {
            answer.append(my_string);
        }
        
        return answer.toString();
    }
}