import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        
		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            int[][] map = new int[N][N];
            String[][] answer = new String[N][3];
            
            for(int i=0;i<N;i++){
            	for( int j=0;j<N;j++){
                	map[i][j] = sc.nextInt();
                }
            }
            
             // 90도 회전
            for (int i = 0; i < N; i++) {
                String temp = "";
                for (int j = N - 1; j >= 0; j--) {
                    temp += map[j][i];
                }
                answer[i][0] = temp;
            }

            // 180도 회전
            for (int i = 0; i < N; i++) {
                String temp = "";
                for (int j = N - 1; j >= 0; j--) {
                    temp += map[N - 1 - i][j];
                }
                answer[i][1] = temp;
            }

            // 270도 회전
            for (int i = 0; i < N; i++) {
                String temp = "";
                for (int j = 0; j < N; j++) {
                    temp += map[j][N - 1 - i];
                }
                answer[i][2] = temp;
            }
            
            System.out.println("#"+test_case);
            for(int i=0;i<N;i++){
            	System.out.println(answer[i][0] +" " + answer[i][1] +" " + answer[i][2]);
            }
		}
	}
}