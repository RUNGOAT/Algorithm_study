import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

	static int N;
	static int[][] arr;
	static boolean[][] visited;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };
	static int count;
	static List<Integer> list = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		arr = new int[N][N];

		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}
		visited = new boolean[N][N];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == 1 && visited[i][j] == false) {
					dfs(i, j);
					list.add(count);
					count = 0;
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		sb.append(list.size() + "\n");
		Collections.sort(list);
		for (int i = 0; i < list.size(); i++) {
			sb.append(list.get(i) + "\n");
		}

		System.out.println(sb);

	}

	static void dfs(int x, int y) {
		visited[x][y] = true;
		count++;
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d], ny = y + dy[d];
			if (0 > nx || N <= nx || 0 > ny || N <= ny)
				continue;
			if (visited[nx][ny])
				continue;
			if (arr[nx][ny] == 0)
				continue;
			dfs(nx, ny);
		}
	}
}
