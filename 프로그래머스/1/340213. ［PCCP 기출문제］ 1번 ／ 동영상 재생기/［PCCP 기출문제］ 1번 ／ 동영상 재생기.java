class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int vl = timeToSeconds(video_len);
        int p = timeToSeconds(pos);
        int os = timeToSeconds(op_start);
        int oe = timeToSeconds(op_end);
        
        if(os <= p && p <= oe) p = oe;
        
        for(String command : commands) {
            switch(command) {
                case "prev":
                    p = p - 10 <= 0 ? 0 : p - 10;
                    break;
                case "next":
                    p = p + 10 >= vl ? vl : p + 10;
                    break;
            }
            if(os <= p && p <= oe) p = oe;
        }
        
        return secondsToTime(p);
    }
    
    private int timeToSeconds(String time) {
        return Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(3, 5));
    }
    
    private String secondsToTime(int seconds) {
        return String.format("%02d:%02d", seconds / 60, seconds % 60);
    }
}