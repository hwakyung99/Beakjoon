class Solution {
    public int solution(int a, int b, int c) {
        int answer = a + b + c;
        
        answer = (a == b || a == c || b == c) ? answer * (int) (Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2)) : answer;
        
        answer = (a == b && b == c) ? answer * (int) (Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3)) : answer;
        
        return answer;
    }
}