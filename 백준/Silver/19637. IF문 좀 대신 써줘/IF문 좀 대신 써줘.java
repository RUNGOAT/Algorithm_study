import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
	String style;
	int power;

	public Node(StringTokenizer st) {
		super();
		this.style = st.nextToken();
		this.power = Integer.parseInt(st.nextToken());
	}
}

public class Main {

	static Node[] node;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		node = new Node[N];
		for (int n = 0; n < N; n++) {
			node[n] = new Node(new StringTokenizer(br.readLine()));
		}
		
		StringBuilder sb = new StringBuilder();
		for (int m = 0; m < M; m++) {
			int power = Integer.parseInt(br.readLine());
			sb.append(binary(power) + "\n");
		}
		System.out.println(sb);
	}

	static String binary(int power) {
		int start = 0, end = node.length - 1;
		while (start < end) {
			int mid = (start + end) / 2;
			if (power > node[mid].power) {
				start = mid + 1;
			} else {
				end = mid;
			}
		}
		return node[end].style;
	}
}
