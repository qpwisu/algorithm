import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        
        Arrays.sort(times);
        
        long left = 1; 
        long right = (long) Arrays.stream(times).max().getAsInt() * n;
        
        while(left <= right){
            // 종료 조건, 시간동
            long tmp = 0; 
            long mid = (long) (left + right) /2 ;
            
            for(int time: times){
                tmp += mid/time;
                
                if(tmp > n){
                    break;
                }
            }
            if (tmp >= n){
                answer = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }            
        }
        return answer;
    }
}