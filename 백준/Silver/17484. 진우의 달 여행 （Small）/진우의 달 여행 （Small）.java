import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M;
	static int[][] arr;
	static int[] dy = { -1, 0, 1 };
	static int min;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		min = 601;
		for (int j = 0; j < M; j++) {
			dfs(0, j, 0, arr[0][j]);
			dfs(0, j, 1, arr[0][j]);
			dfs(0, j, 2, arr[0][j]);
		}
		
		System.out.println(min);
		
	}

	private static void dfs(int x, int y, int dd, int fuel) {
		if (x == N - 1) {
			min = Math.min(min, fuel);
			return;
		}
		
		for (int d = 0; d < 3; d++) {
			if (d == dd)	continue;
			int ny = y + dy[d];
			if (0 > ny || M <= ny)	continue;
			dfs(x + 1, ny, d, fuel + arr[x + 1][ny]);
		}
	}

}
