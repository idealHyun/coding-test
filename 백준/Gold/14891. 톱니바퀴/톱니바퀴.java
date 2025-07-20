import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        Tobni t1 = new Tobni(br.readLine().chars().map(c->c-'0').toArray());
        Tobni t2 = new Tobni(br.readLine().chars().map(c->c-'0').toArray());
        Tobni t3 = new Tobni(br.readLine().chars().map(c->c-'0').toArray());
        Tobni t4 = new Tobni(br.readLine().chars().map(c->c-'0').toArray());
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Tobni[] ts = new Tobni[]{t1,t2,t3,t4};
        
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            int order = Integer.parseInt(st.nextToken()) - 1;
            int way = Integer.parseInt(st.nextToken());
            run(ts,order,way,new boolean[4]);
        }
        
        System.out.println(getScore(ts));
    }
    
    static void run(Tobni[] ts,int order,int way,boolean[] visited){
        visited[order]=true;
        boolean left=false,right=false;
        // 왼쪽 확인
        if(order > 0 && !visited[order-1]){
            if(ts[order-1].items[2]!=ts[order].items[6]){
                left=true;
            }
        }
        
        // 오른쪽 확인
        if(order < 3 && !visited[order+1]){
            if(ts[order+1].items[6]!=ts[order].items[2]){
                right=true;
            }
        }
        
        if(way==1){
            ts[order].right();
        } else{
            ts[order].left();
        }
        
        if(left){
            run(ts,order-1,way * -1,visited);
        }
        if(right){
            run(ts,order+1,way * -1,visited);
        }
    }
    
    static int getScore(Tobni[] ts){
        int sum=0;
        
        for(int i=0;i<ts.length;i++){
            if(ts[i].items[0]==1){
                int k=1;
                for(int j=0;j<i;j++){
                    k*=2;
                }
                sum += k;
            }
        }
        return sum;
    }
    
}

class Tobni{
    int[] items;
    
    public Tobni(int[] items){
        this.items = items;
    }
    
    public void right() {
        int temp = items[7];
        for (int i = 7; i > 0; i--) {
            items[i] = items[i - 1];
        }
        items[0] = temp;
    }
    
    public void left() {
        int temp = items[0];
        for (int i = 0; i < 7; i++) {
            items[i] = items[i + 1];
        }
        items[7] = temp;
    }
}
