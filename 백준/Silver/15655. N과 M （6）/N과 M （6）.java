import java.util.*;
import java.io.*;

class Main {
    static boolean[] visited;
    static int N,M,answer[],arr[];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M =Integer.parseInt(st.nextToken());
        arr = new int[N];
        answer = new int[M];
        visited = new boolean[N];
        
        st = new StringTokenizer(br.readLine());
        
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        
        dfs(0,0);
        
    }
    
    static void dfs(int cnt,int start){
        if(cnt==M){
            for(int n:answer){
                System.out.print(n+" ");
            }
            System.out.println();
            return;
        }
        
        for(int i=start;i<N;i++){
            answer[cnt]=arr[i];
            dfs(cnt+1,i+1);
        }
    }
}