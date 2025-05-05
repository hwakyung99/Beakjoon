class Solution {
    public String solution(String code) {
        char mode = '0';
        StringBuilder ret = new StringBuilder();
        
        for(int i = 0; i < code.length(); i++) {
            if(code.charAt(i) == '1') {
                mode = mode == '1' ? '0' : '1';
                continue;
            }
            if((i + mode - '0') % 2 == 0) {
                ret.append(code.charAt(i));
            }
        }
        
        if(ret.length() == 0) {
            ret.append("EMPTY");
        }
        
        return ret.toString();
    }
}