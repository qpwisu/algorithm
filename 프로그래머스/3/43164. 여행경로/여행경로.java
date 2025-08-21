import java.util.*;
class Solution {
    static String[][] tickets; 
    static boolean[] visited; 
    static Deque<String> path;
    static List<List<String>> pathList;

    static int N; 
    
    private void dfs(){
        String start = path.peekFirst();

        if(path.size() == N+1){
            List<String> q = new ArrayList<>(path);
            pathList.add(q);
            return;
        }
        
        for (int i =0; i<N; i++){
            String[] ticket = tickets[i];
            
            if(ticket[0].equals(start) && visited[i] == false){
                path.push(ticket[1]);
                visited[i] = true;
                dfs();
                path.pop();
                visited[i] = false;
            }
        }
    }
    
    public String[] solution(String[][] tickets) {
        Arrays.sort(tickets,(a,b) -> a[0].compareTo(b[0]));
        visited = new boolean[tickets.length];
        N = tickets.length;
        this.tickets = tickets;
        pathList = new ArrayList<>();
        path = new ArrayDeque<>();
        path.push("ICN");
//         // dfs에서 출발지 입력하면 path에 저장방식? 
        dfs();
        
        for (List<String> pl : pathList){
            Collections.reverse(pl);
        }
        
        pathList.sort((a, b) -> {
        for (int i = 0; i < Math.min(a.size(), b.size()); i++) {
            int cmp = a.get(i).compareTo(b.get(i));
            if (cmp != 0) return cmp;
            }
            return a.size() - b.size();
        });
        
        
        String[] answer = pathList.get(0).toArray(new String[0]);
        return answer;
    }
}