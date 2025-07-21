import java.util.*;
import java.io.*;

class Solution{
    static int[][] map;
    static int[] dy = {0,-1,0,1};
    static int[] dx= {1,0,-1,0};
    
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        
        for(int test_case = 1; test_case <= T; test_case++){
            StringBuilder sb = new StringBuilder();
            int N = Integer.parseInt(br.readLine());
            map = new int[N][N];
            int d=0;
            int y=0;
            int x=0;
            map[y][x]=1;
            
            for(int i=2;i<N*N+1; i++){
                int ny = y+dy[d%4];
                int nx = x+dx[d%4];
                
                while(ny<0 || ny>=N || nx<0 || nx>=N || map[ny][nx]!=0){
                    d++;
                    ny = y + dy[d%4];
                    nx = x + dx[d%4];
                }
                map[ny][nx]=i;
                y = ny;
                x = nx;
            }
            
            sb.append("#" + test_case + "\n");
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    sb.append(map[i][j] + " ");
                }
                sb.append("\n");
            }
            System.out.print(sb.toString());
        }
    }
}