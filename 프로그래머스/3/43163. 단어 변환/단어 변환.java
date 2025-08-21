import java.util.*;

class Solution {
    private boolean canConvert(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i) && ++diff > 1) return false;
        }
        return diff == 1;
    }

    public int solution(String begin, String target, String[] words) {
        boolean exist = false;
        for (String w : words) if (w.equals(target)) { exist = true; break; }
        if (!exist) return 0;

        boolean[] visited = new boolean[words.length];
        Queue<int[]> q = new LinkedList<>(); // [index, depth], begin은 -1
        q.offer(new int[]{-1, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            String curWord = cur[0] == -1 ? begin : words[cur[0]];
            int depth = cur[1];

            if (curWord.equals(target)) return depth;

            for (int i = 0; i < words.length; i++) {
                if (visited[i]) continue;
                if (canConvert(curWord, words[i])) {
                    visited[i] = true;
                    q.offer(new int[]{i, depth + 1});
                }
            }
        }
        return 0;
    }
}