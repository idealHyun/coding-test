import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
    static int[][] map;
    static int N, M;
    static int[] dxCross = { -1, 1, 1, -1};
    static int[] dyCross = { 1, 1, -1, -1};
    static int[] dxAxis = {0, 1, 0, -1};
    static int[] dyAxis = {1, 0, -1, 0};

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            M = sc.nextInt();
            map = new int[N][N];
            int answer = Integer.MIN_VALUE;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = sc.nextInt();
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    answer = Math.max(answer, crossSum(i, j));
                    answer = Math.max(answer, axisSum(i, j));
                }
            }

            System.out.println("#" + test_case + " " + answer);
        }
    }

    static int crossSum(int y, int x) {
        int sum = map[y][x]; 
        for (int i = 0; i < 4; i++) {
            for (int j = 1; j < M; j++) {
                int dy = y + dyCross[i] * j;
                int dx = x + dxCross[i] * j;
                if (dy >= 0 && dy < N && dx >= 0 && dx < N) {
                    sum += map[dy][dx];
                }
            }
        }
        return sum;
    }

    static int axisSum(int y, int x) {
        int sum = map[y][x]; 
        for (int i = 0; i < 4; i++) {
            for (int j = 1; j < M; j++) {
                int dy = y + dyAxis[i] * j;
                int dx = x + dxAxis[i] * j;
                if (dy >= 0 && dy < N && dx >= 0 && dx < N) {
                    sum += map[dy][dx];
                }
            }
        }
        return sum;
    }
}
