import java.util.ArrayList;
import java.util.Collections;

class Solution {
    int l, r;
    ArrayList<Integer> answer = new ArrayList<>();
    
    public int[] solution(int l, int r) {
        
        this.l = l;
        this.r = r;
        
        dfs("");
        
        if(answer.isEmpty()) answer.add(-1);
        Collections.sort(answer);
        return answer.stream().mapToInt(i -> i).toArray();
    }
    
    private void dfs(String s) {
        if(!s.isEmpty()) {
            if(s.equals("0")) return;
            if(Integer.parseInt(s) > r) return;
            if(s.length() > String.valueOf(r).length()) return;
            if(Integer.parseInt(s) >= l && Integer.parseInt(s) <= r) answer.add(Integer.parseInt(s));
        }
        
        dfs(s + "0");
        dfs(s + "5");
    }
}