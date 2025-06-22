import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        int n = 0 ;
        for(int[] c : commands){
            int i = c[0];
            int j = c[1];
            int k = c[2];
            int[] li = Arrays.copyOfRange(array,i-1,j);
            Arrays.sort(li);
            answer[n] = li[k-1];
            n+=1 ;
        }
        
        return answer;
    }
}