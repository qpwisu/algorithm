import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> li = new ArrayList<>();

        // 5의 배수로 시작하도록 보정
        if (l % 5 != 0) {
            l += (5 - l % 5);
        }

        for (int i = l; i <= r; i += 5) {
            String s = String.valueOf(i);
            boolean b = true;
            for (char c : s.toCharArray()) {
                if (c != '0' && c != '5') {
                    b = false;
                    break;
                }
            }
            if (b) li.add(i);
        }

        // 리스트가 비어있으면 -1을 담은 배열 반환
        if (li.isEmpty()) return new int[]{-1};

        // 리스트를 배열로 변환
        return li.stream().mapToInt(i -> i).toArray();
    }
}