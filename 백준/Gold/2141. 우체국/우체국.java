import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	static long X;
	static long A;
	static StringTokenizer st;

	private static class Node {
		long x;
		long a;

		public Node(long x1, long a1) {
			this.x = x1;
			this.a = a1;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Node[] arr = new Node[N];

		long sum = 0;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			X = Long.parseLong(st.nextToken());
			A = Long.parseLong(st.nextToken());
			arr[i] = new Node(X, A);
			sum += A;
		}

		Arrays.sort(arr, new Comparator<Node>() {

			@Override
			public int compare(Node o1, Node o2) {
				if (o1.x == o2.x)
					return (int) (o1.a - o2.a);
				return (int) (o1.x - o2.x);
			}

		});

		long ssum = 0;
		for (int i = 0; i < N; i++) {
			ssum += arr[i].a;
			if (ssum >= (sum + 1) / 2) {
				System.out.println(arr[i].x);
				break;
			}
		}

	}
}
