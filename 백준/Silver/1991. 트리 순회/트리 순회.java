import java.util.*;
import java.io.*;


public class Main {
	
	static void preOrder(char node) {
		if (node != '.') {
			System.out.print(node);
			preOrder(tree.get(node)[0]);
			preOrder(tree.get(node)[1]);
		}
	}

	static void inOrder(char node) {
		if (node != '.') {
			inOrder(tree.get(node)[0]);
			System.out.print(node);
			inOrder(tree.get(node)[1]);
		}
	}

	static void postOrder(char node) {
		if (node != '.') {
			postOrder(tree.get(node)[0]);
			postOrder(tree.get(node)[1]);
			System.out.print(node);
		}
	}
	
	static Map<Character, char[]> tree;
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int N = Integer.parseInt(br.readLine());
    	tree = new HashMap<>();
    	for (int i = 0; i < N; i++) {
    		StringTokenizer st = new StringTokenizer(br.readLine());
    		char root = st.nextToken().charAt(0);
    		char left = st.nextToken().charAt(0);
    		char right = st.nextToken().charAt(0);
    		
    		tree.put(root, new char[] {left, right});
    	}
    	
    	preOrder('A');
    	System.out.println();
    	inOrder('A');
    	System.out.println();
    	postOrder('A');
    	
    	br.close();
    }
}
