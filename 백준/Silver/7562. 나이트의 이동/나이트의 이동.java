import java.util.*;
import java.io.*;

class Main {
    static int[] dx={1,2,2,1,-1,-2,-2,-1};
    static int[] dy={2,1,-1,-2,-2,-1,1,2};
    static int N,answer;
    static boolean[][] visited;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        
        for(int i=0;i<T;i++){
            N = Integer.parseInt(br.readLine());
            visited = new boolean[N][N];
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s_x = Integer.parseInt(st.nextToken());
            int s_y = Integer.parseInt(st.nextToken());
            
            st = new StringTokenizer(br.readLine());
            int e_x = Integer.parseInt(st.nextToken());
            int e_y = Integer.parseInt(st.nextToken());
            
            answer=0;
            bfs(s_y,s_x,e_y,e_x);
            System.out.println(answer);
        }
    }
    
    static void bfs(int s_y, int s_x, int e_y, int e_x) {
    Deque<int[]> q = new ArrayDeque<>();
    q.add(new int[]{s_y, s_x, 0});
    visited[s_y][s_x] = true;

    while (!q.isEmpty()) {
        int[] curr = q.poll();
        int y = curr[0];
        int x = curr[1];
        int count = curr[2];

        if (y == e_y && x == e_x) {
            answer = count;
            return;
        }

        for (int i = 0; i < 8; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny >= 0 && ny < N && nx >= 0 && nx < N && !visited[ny][nx]) {
                visited[ny][nx] = true;
                q.add(new int[]{ny, nx, count + 1});
                }
            }
        }
    }
}