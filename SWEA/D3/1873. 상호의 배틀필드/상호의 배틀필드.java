import java.util.*;
import java.io.*;

public class Solution {
  static char[][] map;
  // 상,우,하 좌
  static int[] dy = { -1, 0, 1, 0 };
  static int[] dx = { 0, 1, 0, -1 };
  static int dir, H, W, y, x;

  public static void main(String args[]) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());

    for (int test_case = 1; test_case <= T; test_case++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      H = Integer.parseInt(st.nextToken());
      W = Integer.parseInt(st.nextToken());
      map = new char[H][W];

      for (int i = 0; i < H; i++) {
        map[i] = br.readLine().toCharArray();
      }

      checkStartPosition();

      int N = Integer.parseInt(br.readLine());
      char[] commands = br.readLine().toCharArray();

      for (char c : commands) {
        switch (c) {
          case 'U':
            move(0);
            break;
          case 'R':
            move(1);
            break;
          case 'D':
            move(2);
            break;
          case 'L':
            move(3);
            break;
          case 'S':
            shoot();
            break;
          default:
            break;
        }
      }

      sb.append("#" + test_case + " ");
      for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
          sb.append(map[i][j]);
        }
        sb.append("\n");
      }

    }
    System.out.print(sb.toString());
  }

  private static void shoot() {
    // 벽 및 맵 밖까지 직진
    int ny = y + dy[dir];
    int nx = x + dx[dir];
    while (ny >= 0 && ny < H && nx >= 0 && nx < W) {
      // 강철벽(#)은 만나고 사라짐
      if (map[ny][nx] == '#') {
        return;
      }
      // 벽돌벽(*)은 만나면 평지로 만들고 사라짐
      else if (map[ny][nx] == '*') {
        map[ny][nx] = '.';
        return;
      } else if (map[ny][nx] == '.' || map[ny][nx] == '-') {
        ny = ny + dy[dir];
        nx = nx + dx[dir];
      }
    }
  }

  private static void move(int i) {
    dir = i;
    int ny = y + dy[i];
    int nx = x + dx[i];

    // 평지 확인, map 빠져나갔는지 확인
    if (ny >= 0 && ny < H && nx >= 0 && nx < W && map[ny][nx] == '.') {
      if (i == 0) {
        map[ny][nx] = '^';
      } else if (i == 1) {
        map[ny][nx] = '>';
      } else if (i == 2) {
        map[ny][nx] = 'v';
      } else if (i == 3) {
        map[ny][nx] = '<';
      }
      map[y][x] = '.';
      y = ny;
      x = nx;
    } else {
      if (i == 0) {
        map[y][x] = '^';
      } else if (i == 1) {
        map[y][x] = '>';
      } else if (i == 2) {
        map[y][x] = 'v';
      } else if (i == 3) {
        map[y][x] = '<';
      }
    }
  }

  private static void checkStartPosition() {
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (map[i][j] == '^') {
          y = i;
          x = j;
          dir = 0;
        }

        if (map[i][j] == '>') {
          y = i;
          x = j;
          dir = 1;
        }

        if (map[i][j] == 'v') {
          y = i;
          x = j;
          dir = 2;
        }

        if (map[i][j] == '<') {
          y = i;
          x = j;
          dir = 3;
        }
      }
    }
  }
}