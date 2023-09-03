import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int answer = 0;
	static final int MAX_ROUND = 5;
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		int[][] firstMap = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				firstMap[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(firstMap, 1);
		
		bw.write(answer + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
	
	static void dfs(int[][] map, int round) {
		if (round > MAX_ROUND) {
			answer = Math.max(answer, getAnswer(map));
			return;
		}
		
		// 오 -> 왼
		dfs(moveColumn(map, N-1, -1, -1), round+1);
		
		// 왼 -> 오
		dfs(moveColumn(map, 0, N, 1), round+1);
		
		// 위 -> 아래
		dfs(moveRow(map, 0, N, 1), round+1);
		
		// 아래 -> 위
		dfs(moveRow(map, N-1, -1, -1), round+1);
	}
	
	static int[][] moveColumn(int[][] map, int cs, int ce, int next) {
		int[][] newMap = copy(map);
		for (int i = 0; i < N; i++) {
			int idx = cs;
			int value = -1;
			for (int j = cs; j != ce; j += next) {
				if (newMap[i][j] == 0)	continue;
				if (value == -1) {
					value = newMap[i][j];
					continue;
				}
				if (value == newMap[i][j]) {
					newMap[i][idx] = value * 2;
					idx += next;
					value = -1;
				} else {
					newMap[i][idx] = value;
					idx += next;
					value = newMap[i][j];
				}
			}
			if (value > 0) {
				newMap[i][idx] = value;
				idx += next;
			}
			for (int j = idx; j != ce; j += next) {
				newMap[i][j] = 0;
			}
		}
		return newMap;
	}
	
	static int[][] moveRow(int[][] map, int rs, int re, int next) {
		int[][] newMap = copy(map);
		for (int j = 0; j < N; j++) {
			int idx = rs;
			int value = -1;
			for (int i = rs; i != re; i += next) {
				if (newMap[i][j] == 0)	continue;
				if (value == -1) {
					value = newMap[i][j];
					continue;
				}
				if (value == newMap[i][j]) {
					newMap[idx][j] = value * 2;
					idx += next;
					value = -1;
				} else {
					newMap[idx][j] = value;
					idx += next;
					value = newMap[i][j];
				}
			}
			if (value > 0) {
				newMap[idx][j] = value;
				idx += next;
			}
			for (int i = idx; i != re; i += next) {
				newMap[i][j] = 0;
			}
		}
		return newMap;
	}
	
	static int getAnswer(int[][] map) {
		int ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (ans < map[i][j]) {
					ans = map[i][j];
				}
			}
		}
		return ans;
	}
	
	static int[][] copy(int[][] map) {
		int[][] copy = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				copy[i][j] = map[i][j];
			}
		}
		return copy;
	}
}
