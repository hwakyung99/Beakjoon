import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        Deque<Character> stack = new ArrayDeque<Character>();
        
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                stack.addFirst(s.charAt(i));
            }
            else if(s.charAt(i) == ')') {
                if(stack.isEmpty()){
                    answer = false;
                    break;
                }
                else {
                    stack.removeFirst();
                }
            }
        }
        
        if(!stack.isEmpty()) answer = false;
        
        return answer;
    }
}