import java.util.*;
import java.io.*;

public class Main {

	static int N, K, answer;
	static List<int[]>[] colors;

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		answer = Integer.MAX_VALUE;
		colors = new ArrayList[K + 1];
		for (int i = 1; i <= K; i++) {
			colors[i] = new ArrayList<>();
		}

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());

			colors[k].add(new int[] { x, y });
		}

		dfs(1, 1000, -1000, 1000, -1000);
        System.out.println(answer);
	}

	static void dfs(int color, int left, int right, int bottom, int top) {
		if (color == K + 1) {
			return;
		}
		for (int[] point : colors[color]) {
			int x = point[0], y = point[1];
			int leftN = Math.min(left, x);
			int rightN = Math.max(right, x);
			int bottomN = Math.min(bottom, y);
			int topN = Math.max(top, y);
			int area = (rightN - leftN) * (topN - bottomN);
			if (answer > area) {
				if (color == K) {
					answer = Math.min(answer, area);
				}
				dfs(color + 1, leftN, rightN, bottomN, topN);
			}
		}
	}
  
}
