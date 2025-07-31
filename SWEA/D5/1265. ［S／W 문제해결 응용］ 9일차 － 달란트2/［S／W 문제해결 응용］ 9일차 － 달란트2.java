import java.util.*;
import java.io.*;

public class Solution {
    static int N, P;

    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());

            sb.append("#" + t + " " + dalant(N, P)).append("\n");
        }
        System.out.println(sb.toString());
    }

    private static long dalant(int n, int p) {
        if (p == 1)
            return n;
        return (n / p) * dalant(n - (n / p), p - 1);
    }
}