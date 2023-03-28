import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int M;
	static int[][] arr;
	static int[][] visited;
	static Queue<int[]> queue;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };

	static int bfs(int x, int y) {
		visited = new int[N][M];
		visited[x][y] = 1;
		queue = new LinkedList<>();
		queue.add(new int[] { x, y });
		int temp = 0;
		while (!queue.isEmpty()) {
			int[] now = queue.poll();
			if (now[0] == N - 1 && now[1] == M - 1) {
				temp = visited[now[0]][now[1]];
				break;
			}
			for (int i = 0; i < 4; i++) {
				int nx = now[0] + dx[i];
				int ny = now[1] + dy[i];
				if (0 > nx || nx >= N || 0 > ny || ny >= M)
					continue;
				if (visited[nx][ny] == 0 && arr[nx][ny] == 1) {
					visited[nx][ny] = visited[now[0]][now[1]] + 1;
					queue.offer(new int[] { nx, ny });
				}
			}
		}
		return temp;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}

		System.out.println(bfs(0, 0));

	}

}
