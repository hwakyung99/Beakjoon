import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        Deque<Integer> stack = new ArrayDeque<>();

        stack.addLast(arr[0]);
        for(int i : arr) {
            if(stack.peekLast() != i) stack.addLast(i);
        }

        return stack.stream().mapToInt(j -> j).toArray();
    }
}