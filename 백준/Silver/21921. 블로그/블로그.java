import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, X;
	static int[] arr;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());

		arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		int maxVisitor = 0;
		int maxCount = 1;
		for (int x = 0; x < X; x++) {
			maxVisitor += arr[x];
		}

		int sum = maxVisitor;
		for (int i = 0; i < N - X; i++) {
			int visitor = sum;
			visitor -= arr[i];
			visitor += arr[i + X];
			if (maxVisitor < visitor) {
				maxVisitor = visitor;
				maxCount = 1;
			} else if (maxVisitor == visitor) {
				maxCount++;
			}
			sum = visitor;
		}

		if (maxVisitor == 0) {
			System.out.println("SAD");
		} else {
			System.out.println(maxVisitor);
			System.out.println(maxCount);
		}
	}

}
