import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	static int[] number = { 1, 5, 10, 50 };
	static int[] arr;
	static int answer;
	static boolean visited[];

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		arr = new int[N];
		answer = 0;
		visited = new boolean[1001];

		dfs(N, 0, 0);
		
		System.out.println(answer);
	}

	static void dfs(int n, int index, int sum) {
		if (n == 0) {
			if (!visited[sum]) {
				answer++;
				visited[sum] = true;
			}
			return;
		}
		
		for (int i = index; i < 4; i++) {
			dfs(n-1, i, sum + number[i]);
		}
	}

}
