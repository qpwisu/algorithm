import java.util.*;

/*
4 7
6 13
4 8
3 6
5 12
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[][] bags = new int[N][2];
        for (int i = 0; i < N; i++) {
            int w = sc.nextInt();
            int v = sc.nextInt();
            bags[i][0] = w;
            bags[i][1] = v;
        }

        int [] dp= new int[K+1];

        for (int [] bag: bags) {
            // newdp를 쓰는 이유는 같은 아이템을 한번 쓰기 위해서임, 여러번 쓸수 있으면 dp만 사용
            int [] newDp = dp.clone();
            int w = bag[0];
            int v = bag[1];
            // newDp를 씀으로서 방금 갱신된 값을 다시한번 사용하지 않게함
            // 예시 dp[2]에서 넣은 물건을 dp[2+2]에서 다시한번 넣으려할 수 있음 그래서 dp[2]를 newDp에 넣는거
            for (int i = 0; i < K+1;i++){
                if (K >= w+i){
                    newDp[w+i] = Math.max(newDp[w+i], dp[i]+v);
                }
            }
            dp = newDp;
        }

        System.out.println(dp[K]);

    }
}