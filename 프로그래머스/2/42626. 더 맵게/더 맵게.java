import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        
        for (int scov : scoville){
            queue.add(scov);
        }
                
        while (true){
            if (queue.size()==1){
                if (queue.peek() < K){
                    return -1;
                }
                break;
            }
                        
            Integer first = queue.poll();
            if (first >= K){
                return answer;
            }
            
            Integer second = queue.poll();
            
            queue.add(first + second*2);
            answer +=1 ;
            
        }
        
        return answer;
    }
}