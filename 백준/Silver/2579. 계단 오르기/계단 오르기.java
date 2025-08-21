import java.util.*;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n+1];
        arr[0] = 0;
        for (int i = 0; i < n; i++) {
            arr[i+1] = sc.nextInt();
        }
        if (n == 1) { System.out.println(arr[1]); return; }
        if (n == 2) { System.out.println(arr[1] + arr[2]); return; }


        int[] dp = new int[n+1];
        Arrays.fill(dp,-1);
        dp[0] = 0;
        dp[1] = arr[1];
        dp[2] = arr[1] + arr[2];

        for (int i = 3; i <n+1; i++) {
            int jump = dp[i-2] + arr[i];
            int step = dp[i-3] + arr[i-1]+ arr[i];
            if (jump > step) {
                if (jump > dp[i]){
                    dp[i] = jump;
                }
            }
            else{
                if (step > dp[i]){
                    dp[i] = step;
                }
            }
        }

        System.out.println(dp[n]);
    }
}