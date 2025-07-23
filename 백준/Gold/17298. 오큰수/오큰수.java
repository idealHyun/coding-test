import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        List<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        for (int i = N - 1; i >= 0; i--) {
            int num;
            while (true) {
                if (stack.isEmpty()) {
                    num = -1;
                    break;
                }

                if (stack.peek() <= arr[i]) {
                    stack.pop();
                } else {
                    num = stack.peek();
                    break;
                }
            }

            stack.add(arr[i]);
            answer.add(num);
        }

        for (int i = N - 1; i >= 0; i--) {
            sb.append(answer.get(i) + " ");
        }
        System.out.print(sb.toString());
    }
}
