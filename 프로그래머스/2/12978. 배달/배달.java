import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        // 그래프: graph[u] = { {v, w}, ... }
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) graph.add(new ArrayList<>());

        for (int[] r : road) {
            int a = r[0], b = r[1], w = r[2];
            graph.get(a).add(new int[]{b, w});
            graph.get(b).add(new int[]{a, w}); // 양방향
        }

        final int INF = 1_000_000_000;
        int[] dist = new int[N + 1];
        Arrays.fill(dist, INF);
        dist[1] = 0;

        // pq: {노드, 현재까지의 최단거리} — 거리 오름차순
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{1, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0];
            int d = cur[1];

            // 스테일(오래된) 항목 스킵
            if (d != dist[u]) continue;

            for (int[] e : graph.get(u)) {
                int v = e[0], w = e[1];
                int nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new int[]{v, nd});
                }
            }
        }

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            if (dist[i] <= K) answer++;
        }
        return answer;
    }
}