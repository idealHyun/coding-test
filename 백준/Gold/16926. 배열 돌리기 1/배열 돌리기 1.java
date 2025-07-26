import java.io.*;
import java.util.*;

public class Main {
    static int N, M, R;
    static int[][] map;
    static int[] dy = new int[] { 1, 0, -1, 0 };
    static int[] dx = new int[] { 0, 1, 0, -1 };

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            map[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for (int i = 0; i < R; i++) {
            rotate();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(map[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    private static void rotate() {
        boolean[][] visited = new boolean[N][M];
        int[][] tempMap = new int[N][M];
        int y = 0;
        int x = 0;
        while (!visited[y][x]) {
            dfs(y, x, 0, tempMap, visited);
            y++;
            x++;
        }
        map = tempMap;
    }

    private static void dfs(int y, int x, int d, int[][] tempMap, boolean[][] visited) {
        if (d == 4)
            return;

        int ny = y + dy[d];
        int nx = x + dx[d];
        if (isValid(ny, nx, visited)) {
            visited[ny][nx] = true;
            // map에서 가져와서 대입하는 코드 넣기
            tempMap[ny][nx] = map[y][x];
            dfs(ny, nx, d, tempMap, visited);
        } else {
            dfs(y, x, d + 1, tempMap, visited);
        }

    }

    private static boolean isValid(int ny, int nx, boolean[][] visited) {
        return ny >= 0 && ny < N && nx >= 0 && nx < M && !visited[ny][nx];
    }
}
