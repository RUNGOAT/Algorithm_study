import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	private static final int[] DX = { 0, -1, 0, 1 };
	private static final int[] DY = { 1, 0, -1, 0 };
	private static final int GRID_SIZE = 101;

	static boolean[][] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine());
		visited = new boolean[GRID_SIZE][GRID_SIZE];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int y = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());

			makeDragonCurve(x, y, d, g);
		}

		bw.write(checkAnswer() + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

	private static void makeDragonCurve(int x, int y, int d, int g) {
		visited[x][y] = true;
		int nx = x + DX[d];
		int ny = y + DY[d];
		visited[nx][ny] = true;
		x = nx;
		y = ny;

		List<Integer> directions = new ArrayList<>();
		directions.add(d);

		for (int i = 0; i < g; i++) {
			List<Integer> newDirections = new ArrayList<>();
			for (int idx = directions.size() - 1; idx >= 0; idx--) {
				d = (directions.get(idx) + 1) % 4;
				nx = x + DX[d];
				ny = y + DY[d];
				visited[nx][ny] = true;
				x = nx;
				y = ny;
				newDirections.add(d);
			}
			directions.addAll(newDirections);
		}
	}

	private static int checkAnswer() {
		int answer = 0;
		for (int i = 0; i < GRID_SIZE - 1; i++) {
			for (int j = 0; j < GRID_SIZE - 1; j++) {
				if (visited[i][j] && visited[i][j + 1] && visited[i + 1][j] && visited[i + 1][j + 1]) {
					answer++;
				}
			}
		}
		return answer;
	}
}
