import java.util.*;
class Node{
    String word;
    int depth;
    int[] visited;
    
    Node(String word, int depth, int[] visited) {
        this.word = word;
        this.depth = depth;
        this.visited = visited.clone(); // 배열 복사 (원본 안 망가뜨리기)
    }
}


class Solution {
    

    private boolean compare(String word, String word2){
        int count = 0;
        
        for (int i =0; i<word.length();i++){
            
            if (word.charAt(i)!=word2.charAt(i)){
                count+=1; 
                
            }
        }
        
        if (count != 1) return false;
        
        return true;
    }
    public int solution(String begin, String target, String[] words) {
        
        int answer = 0;
        Queue<Node> q = new LinkedList<>();
        int[] visited = new int[words.length];
        Node node = new Node(begin,0,visited);
        q.offer(node);
        
        outer:
        while(!q.isEmpty()){
            Node now = q.poll();
            String word = now.word;
            System.out.println(word);
            
            for (int i =0; i< words.length; i++){
                 if (visited[i] == 1){
                     continue;
                 }
                
                boolean cp = compare(word, words[i]);
                
                if (cp){
                    
                    if (target.equals(words[i])){
                        answer = now.depth+1;
                        System.out.println(Arrays.toString(visited));
                        return answer;
                    }
                    
                    visited[i] = 1; 
                    Node node2 = new Node(words[i], now.depth+1 ,visited);
                    q.offer(node2);
                    
                }
                // word랑 비교해서 변환가능한지 확인하는 함수 
                
            }
            
        }
        
        return answer;
    }
}