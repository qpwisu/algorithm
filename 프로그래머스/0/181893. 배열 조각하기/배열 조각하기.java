import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = {};
        int N = query.length;
        
        for (int i = 0; i< N; i++){
            
            if (i%2==0){
                arr = Arrays.copyOfRange(arr,0,query[i] + 1);
            }
            else{
                arr = Arrays.copyOfRange(arr,query[i],arr.length);

            }
        }
        answer = arr;
        
        return answer;
    }
}