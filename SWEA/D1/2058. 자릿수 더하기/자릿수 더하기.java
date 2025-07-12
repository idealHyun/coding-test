import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        Scanner sc = new Scanner(System.in);
        int sum=0;
        char[] input = sc.next().toCharArray();
        
        for (char c : input){
            sum += c - '0';
        }
        
        System.out.println(sum);
	}
}
