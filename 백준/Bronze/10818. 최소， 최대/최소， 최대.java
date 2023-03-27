import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split(" ");

		int min = 1000000;
		int max = -1000000;
		for (int i = 0; i < N; i++) {
			int number = Integer.parseInt(arr[i]);
			if (number > max)
				max = number;
			if (number < min)
				min = number;
		}

		System.out.println(min + " " + max);

	}
}
