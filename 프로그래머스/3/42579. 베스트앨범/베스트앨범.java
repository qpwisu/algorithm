import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 많은 재생된 장르 리스트
        List<Integer> answer = new ArrayList<>();
        int n = genres.length;
        
        Map<String,List<List<Integer>>> map = new HashMap<>();
        
        for(int i=0; i<n; i++){
            if (!map.containsKey(genres[i])) map.put(genres[i],new ArrayList<>());
            map.get(genres[i]).add(Arrays.asList(plays[i],i));
        }
        
        List<List<Object>> genresCount = new ArrayList<>();
        
        for (Map.Entry<String, List<List<Integer>>> entry : map.entrySet()){
            Integer count = 0;
            for( List<Integer> li : entry.getValue()){
                count += li.get(0);
            }
            genresCount.add(Arrays.asList(entry.getKey(),count));
        }
        
        genresCount.sort((a,b) -> (Integer) b.get(1) -(Integer)  a.get(1));
        
            
                        
        System.out.println(genresCount);               
        System.out.println(map);     

        for (List<Object> gc : genresCount){
            map.get(gc.get(0)).sort((a,b) -> b.get(0)-a.get(0));
            
            if (map.get(gc.get(0)).size() == 1 ){
                answer.add((Integer) map.get(gc.get(0)).get(0).get(1));
            }
            else{
                answer.add((Integer) map.get(gc.get(0)).get(0).get(1));
                answer.add((Integer) map.get(gc.get(0)).get(1).get(1));
            }
        }
        System.out.println(answer);               

        int[] answers = answer.stream().mapToInt(i->i).toArray();
        return answers;
    }
}