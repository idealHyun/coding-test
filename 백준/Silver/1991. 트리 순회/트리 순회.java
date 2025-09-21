import java.util.*;
import java.io.*;

class Main {
    static int N;
    static StringBuilder sb;
    static Map<String, Node> nodeMap = new HashMap<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String parent = st.nextToken();
            String left = st.nextToken();
            String right = st.nextToken();

            nodeMap.putIfAbsent(parent, new Node(parent));
            Node parentNode = nodeMap.get(parent);

            if (!left.equals(".")) {
                nodeMap.putIfAbsent(left, new Node(left));
                Node leftNode = nodeMap.get(left);
                parentNode.addLeft(leftNode);
            }

            if (!right.equals(".")) {
                nodeMap.putIfAbsent(right, new Node(right));
                Node rightNode = nodeMap.get(right);
                parentNode.addRight(rightNode);
            }
        }

        preorder(nodeMap.get("A"));
        sb.append("\n");
        middleorder(nodeMap.get("A"));
        sb.append("\n");
        postorder(nodeMap.get("A"));

        System.out.println(sb.toString());
    }

    public static void preorder(Node node) {
        sb.append(node.value);
        if (node.left != null) {
            preorder(node.left);
        }
        if (node.right != null) {
            preorder(node.right);
        }
    }

    public static void middleorder(Node node) {
        if (node.left != null) {
            middleorder(node.left);
        }
        sb.append(node.value);
        if (node.right != null) {
            middleorder(node.right);
        }
    }

    public static void postorder(Node node) {
        if (node.left != null) {
            postorder(node.left);
        }

        if (node.right != null) {
            postorder(node.right);
        }
        sb.append(node.value);
    }

}

class Node {
    String value;
    Node left, right;

    public Node(String value) {
        this.value = value;
    }

    public void addRight(Node node) {
        right = node;
    }

    public void addLeft(Node node) {
        left = node;
    }
}