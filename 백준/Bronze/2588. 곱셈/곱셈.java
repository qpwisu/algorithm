import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        String c = Integer.toString(b);

        for (int i = 2; i >= 0; i--) {
            int f = a * (c.charAt(i) - '0'); // 자리값 보정 제거
            System.out.println(f);
        }

        System.out.println(a * b); // 최종 곱셈 결과 출력
    }
}