import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static StringTokenizer st;

	private static class Node implements Comparable<Node> {
		int x, a;

		public Node(int x1, int a1) {
			this.x = x1;
			this.a = a1;
		}

		@Override
		public int compareTo(Node o) {
			return this.x - o.x;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Node[] arr = new Node[N];
		long total = 0;
		long sum = 0;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			arr[i] = new Node(x, a);
			total += a;
		}

		Arrays.sort(arr);

		for (int i = 0; i < N; i++) {
			sum += arr[i].a;
			if (sum >= (total + 1) / 2) {
				System.out.println(arr[i].x);
				break;
			}
		}
		br.close();
	}
}
