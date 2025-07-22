import java.util.*;
import java.io.*;

class Main {
    static int[][] map;
    static int a_x, a_y;
    static int[] dy = { -1, 0, 1, 0 };
    static int[] dx = { 0, 1, 0, -1 };

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int A = Integer.parseInt(br.readLine());

        map = new int[N][N];
        int m_y = (N - 1) / 2;
        int m_x = (N - 1) / 2;

        int y = m_y;
        int x = m_x;
        int cnt = 1;
        map[y][x] = cnt;
        if (cnt == A) {
            a_y = y + 1;
            a_x = x + 1;
        }
        cnt++;

        int length = 1;
        int d = 0;

        while (cnt <= N * N) {
            for (int repeat = 0; repeat < 2; repeat++) {
                for (int i = 0; i < length; i++) {
                    y += dy[d];
                    x += dx[d];

                    if (y < 0 || x < 0 || y >= N || x >= N)
                        continue;

                    map[y][x] = cnt;
                    if (cnt == A) {
                        a_y = y + 1;
                        a_x = x + 1;
                    }

                    cnt++;
                }

                d = (d + 1) % 4;
            }
            length++;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(map[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
        System.out.println(a_y + " " + a_x);
    }
}
