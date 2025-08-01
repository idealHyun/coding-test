import java.util.*;
import java.io.*;

public class Main {
    static int N, M, R;
    static int[][] map;
    static int[][] temp;

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

        int[] commands = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        for (int command : commands) {
            switch (command) {
                case 1:
                    temp = new int[N][M];
                    firstCommand();
                    break;
                case 2:
                    temp = new int[N][M];
                    secondCommand();
                    break;
                case 3:
                    temp = new int[M][N];
                    thirdCommand();
                    break;
                case 4:
                    temp = new int[M][N];
                    fourthCommand();
                    break;
                case 5:
                    temp = new int[N][M];
                    fifthCommand();
                    break;
                case 6:
                    temp = new int[N][M];
                    sixthCommand();
                    break;
            }
        }

        // 출력
        for (int[] row : map) {
            for (int val : row) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }

    private static void firstCommand() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                temp[N - 1 - i][j] = map[i][j];
            }
        }
        map = temp;
    }

    private static void secondCommand() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                temp[i][M - 1 - j] = map[i][j];
            }
        }
        map = temp;
    }

    private static void thirdCommand() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                temp[j][N - 1 - i] = map[i][j];
            }
        }
        int t = N;
        N = M;
        M = t;
        map = temp;
    }

    private static void fourthCommand() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                temp[M - 1 - j][i] = map[i][j];
            }
        }
        int t = N;
        N = M;
        M = t;
        map = temp;
    }

    private static void fifthCommand() {
        int n2 = N / 2;
        int m2 = M / 2;
        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < m2; j++) {
                temp[i][j + m2] = map[i][j]; // 1 -> 2
                temp[i + n2][j + m2] = map[i][j + m2]; // 2 -> 3
                temp[i + n2][j] = map[i + n2][j + m2]; // 3 -> 4
                temp[i][j] = map[i + n2][j]; // 4 -> 1
            }
        }
        map = temp;
    }

    private static void sixthCommand() {
        int n2 = N / 2;
        int m2 = M / 2;
        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < m2; j++) {
                temp[i + n2][j] = map[i][j]; // 1 -> 4
                temp[i + n2][j + m2] = map[i + n2][j]; // 4 -> 3
                temp[i][j + m2] = map[i + n2][j + m2]; // 3 -> 2
                temp[i][j] = map[i][j + m2]; // 2 -> 1
            }
        }
        map = temp;
    }
}
