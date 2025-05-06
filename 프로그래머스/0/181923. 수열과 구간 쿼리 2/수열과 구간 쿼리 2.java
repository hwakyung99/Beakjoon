import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for(int i = 0; i < queries.length; i++) {
            int s = queries[i][0], e = queries[i][1], k = queries[i][2];
            int tmp = 1000001;
            
            for(int j = s; j < e + 1; j++) {
                if(arr[j] > k && arr[j] < tmp) tmp = arr[j];
            }
            answer.add(tmp == 1000001 ? -1 : tmp);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}