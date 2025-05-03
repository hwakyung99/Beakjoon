class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder ans = new StringBuilder(my_string);
        
        ans.delete(s, s + overwrite_string.length()).insert(s, overwrite_string);
        
        return ans.toString();
    }
}