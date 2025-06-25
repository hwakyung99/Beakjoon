class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder tmpString = new StringBuilder(my_string);
        
        int s, e;
        
        for(int[] query : queries) {
            s = query[0]; e = query[1];
            while(s < e) {
                char tmp = tmpString.charAt(s);
                tmpString.setCharAt(s, tmpString.charAt(e));
                tmpString.setCharAt(e, tmp);
                s++; e--;
            }
        }
        
        return tmpString.toString();
    }
}