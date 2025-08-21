import java.io.*;
import java.util.*;

public class Main {

    static boolean[] visited;
    static int[] output;
    static int[] nums;
    static int n, m;
    static StringBuilder sb = new StringBuilder();

    static void permutation(int depth) { // depth == 현재 뽑은 개수
        if (depth == m) { // 기저 조건
            for (int i = 0; i < m; i++) {
                if (i > 0) sb.append(' ');
                sb.append(output[i]);
            }
            sb.append('\n');
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            output[depth] = nums[i];
            permutation(depth + 1);
            visited[i] = false;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        n = fs.nextInt();
        m = fs.nextInt();

        // 가드: m > n이면 중복 없는 순열은 불가능 → 출력 없음(문제 조건에 따라 처리)
        if (m > n) { 
            // System.out.print(""); 
            return;
        }

        nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = i + 1;

        visited = new boolean[n];
        output = new int[m];

        permutation(0);

        System.out.print(sb);
    }

    // 빠른 입력
    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        FastScanner(InputStream is) { in = is; }
        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
        int nextInt() throws IOException {
            int c, sign = 1, val = 0;
            do c = read(); while (c <= ' '); // skip spaces/newlines
            if (c == '-') { sign = -1; c = read(); }
            while (c > ' ') { val = val * 10 + (c - '0'); c = read(); }
            return val * sign;
        }
    }
}