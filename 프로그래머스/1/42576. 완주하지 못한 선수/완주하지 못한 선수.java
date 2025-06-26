import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // participant를 Map<String, Integer>로 변환 (이름, 개수)
        Map<String, Integer> map = new HashMap<>();
        for(String p : participant) {
            int v = 1;
            if(map.containsKey(p)) v = map.get(p) + 1;
            map.put(p, v);
        }
        
        // completion과 비교
        for(String c : completion) {
            map.replace(c, map.get(c) - 1);
        }

        
        for(String k : map.keySet()) {
            if(map.get(k) > 0) return k;
        }
     
        return null;
    }
}