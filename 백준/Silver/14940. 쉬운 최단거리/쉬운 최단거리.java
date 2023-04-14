import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair {
	int x, y;

	public Pair(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}

}

public class Main {

	static int N;
	static int M;
	static int[][] arr;
	static int[][] visited;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N][M];

		int[] tgt = null;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 2) {
					tgt = new int[] { i, j };
				}
			}
		}

		bfs(tgt);
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 0 && visited[i][j] == -1) {
					visited[i][j] = 0;
				}
				System.out.print(visited[i][j] + " ");
			}
			System.out.println();
		}
	}

	static void bfs(int[] tgt) {
		Queue<Pair> q = new LinkedList<Pair>();
		q.add(new Pair(tgt[0], tgt[1]));
		visited = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				visited[i][j] = -1;
			}
		}
		visited[tgt[0]][tgt[1]] = 0;

		while (!q.isEmpty()) {
			Pair pair = q.poll();
			for (int d = 0; d < 4; d++) {
				int nx = pair.x + dx[d];
				int ny = pair.y + dy[d];
				if (nx < 0 || nx >= N || ny < 0 || ny >= M)
					continue;
				if (visited[nx][ny] != -1)
					continue;
				if (arr[nx][ny] == 1) {
					visited[nx][ny] = visited[pair.x][pair.y] + 1;
					q.add(new Pair(nx, ny));
				}
			}
		}
	}
}
