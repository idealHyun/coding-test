import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static int N, M;
    static int[] arr;
    static int[] cur;
    static StringBuilder sb;
    static Set<List<Integer>> answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        cur = new int[M];
        answer = new LinkedHashSet<List<Integer>>();
        Arrays.sort(arr);

        // cnt, index
        dfs(0, 0);

        for (List<Integer> list : answer) {
            for (int i : list) {
                sb.append(i + " ");
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }

    private static void dfs(int depth, int startIndex) {
        if (depth == M) {
            answer.add(Arrays.stream(cur).boxed().collect(Collectors.toList()));
            return;
        }

        for (int i = startIndex; i < N; i++) {
            cur[depth] = arr[i];
            dfs(depth + 1, i);
            cur[depth] = 0;
        }
    }
}
