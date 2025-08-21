import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        
        int answer = 0;
        int N = maps.length; 
        int M = maps[0].length;
        
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        Queue<List<Integer>> q = new LinkedList<>();
        q.offer(Arrays.asList(0,0));

        while (!q.isEmpty()){
            
            List<Integer> now = q.poll();
            
            for (int i = 0; i<4; i++){
                
                int mx = now.get(0) + dx[i];
                int my = now.get(1) + dy[i];
                
                if ( 0<= mx && mx< M && 0<= my && my< N && maps[my][mx] == 1){
                    
                    q.offer(Arrays.asList(mx,my));
                    maps[my][mx] = maps[now.get(1)][now.get(0)] + 1; 

                }
            }   
        }        
        
        if (maps[N-1][M-1] == 1){
            answer = -1;
        }
        else{
            answer = maps[N-1][M-1];
        }
        
        return answer;
    }
}