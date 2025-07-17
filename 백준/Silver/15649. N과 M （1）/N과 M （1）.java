import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] nums;   
    static boolean[] visited; 
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M =Integer.parseInt(st.nextToken());

        nums =new int[M];
        visited = new boolean[N + 1];

        dfs(0);
        System.out.print(sb.toString());
    }

    static void dfs(int depth) {
        if (depth == M) {
            for (int n: nums) {
                sb.append(n).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i=1; i<= N; i++) { 
            if (visited[i]) continue;
            visited[i]=true;       
            nums[depth]=i;    
            dfs(depth+1);          
            visited[i]=false;      
        }
    }
}