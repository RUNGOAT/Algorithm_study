import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] arr = new int[N];
		int max = 0;
		int min = 1;

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if (arr[i] > max)
				max = arr[i];
		}

		while (min <= max) {
			int mid = (min + max) / 2;

			long sum = 0;
			for (int high : arr) {
				if (high > mid)
					sum += high - mid;
			}

			if (sum >= M)
				min = mid + 1;
			else
				max = mid - 1;
		}

		System.out.println(max);

	}
}
