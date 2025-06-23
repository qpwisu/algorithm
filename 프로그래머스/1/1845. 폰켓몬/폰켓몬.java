import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        List<Integer> numsList = new ArrayList<>();
        
        for (int n : nums) numsList.add(n);
        
        
        int N = nums.length/2;
        Set<Integer> set = new HashSet<>(numsList);
        
        if (set.size() >=N){
            return N;
        }
        else{
            return set.size();
        }
        
    }
}