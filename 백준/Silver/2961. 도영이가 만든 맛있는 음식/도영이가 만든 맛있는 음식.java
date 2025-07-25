import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] ingredients;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        ingredients = new int[N][2];

        for (int i = 0; i < N; i++) {
            ingredients[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        // s는 곱하고 b 는 더하기
        // depth, s,b,count
        dfs(0, 1, 0, 0);

        System.out.println(answer);
    }

    private static void dfs(int depth, int s, int b, int count) {
        if (count != 0) {
            if (s - b >= 0) {
                answer = Math.min(answer, s - b);
            } else {
                answer = Math.min(answer, b - s);
            }
        }

        if (depth == N)
            return;

        dfs(depth + 1, s * ingredients[depth][0], b + ingredients[depth][1], count + 1);
        dfs(depth + 1, s, b, count);
    }
}
