import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] arr;
    static int[] answer;
    static StringBuilder sb;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        answer = new int[M];

        Arrays.sort(arr);

        dfs(0);
        System.out.print(sb.toString());
    }

    private static void dfs(int cnt) {
        if (cnt == M) {
            for (int n : answer) {
                sb.append(n).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 0; i < N; i++) {
            answer[cnt] = arr[i];
            dfs(cnt + 1);
            answer[cnt] = 0;
        }

    }
}
