import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] nums = Arrays.stream(numbers)
                              .boxed()
                              .map(String::valueOf)
                              .sorted((a, b) -> (b + a).compareTo(a + b)) 
                              .toArray(String[]::new);
        
        String result = String.join("", nums);  // 구분자 없이 붙임
        if (nums[0].equals("0")) return "0";
        return result;
    }
}