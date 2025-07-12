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
            int M = sc.nextInt();
            int[] arr1 = new int[N];
            int[] arr2 = new int[M];
            
            for(int i=0;i<N;i++){
                arr1[i]=sc.nextInt();
            }
            
            for(int i=0;i<M;i++){
                arr2[i]=sc.nextInt();
            }
            
            int answer = Integer.MIN_VALUE;
            
            if(N>M){
            	for(int i=0; i<N-M+1;i++){
                    int sum = 0;
                    for(int j=0; j<M; j++){
                        sum += arr1[i + j] * arr2[j];
                    }
                    
                    if(sum > answer){
                        answer = sum;
                    }
                }
            } 
            else{
            	for(int i=0; i<M-N+1;i++){
                    int sum = 0;
                    for(int j=0; j<N; j++){
                        sum += arr2[i + j] * arr1[j];
                    }
                    
                    if(sum > answer){
                        answer = sum;
                    }
                }
            }

			System.out.println("#" + test_case + " " + answer);
		}
	}
}