import java.util.*;

class Solution {
    public int solution(int[] cards) {       
        boolean [] visited = new boolean[cards.length];
        ArrayList<Integer> cnts = new ArrayList<>();
        
        for(int i = 0; i < cards.length; i++) {
            if(!visited[i]) cnts.add(dfs(i, cards, visited));
        }
        
        if(cnts.size() == 1) return 0;
        
        cnts.sort(Comparator.reverseOrder());
        return cnts.get(0) * cnts.get(1);
    }
    
    public int dfs(int n, int[] cards, boolean[] visited) {
        visited[n] = true;
        if(visited[cards[n] - 1]) return 1;
        return 1 + dfs(cards[n] - 1, cards, visited);
    }
}