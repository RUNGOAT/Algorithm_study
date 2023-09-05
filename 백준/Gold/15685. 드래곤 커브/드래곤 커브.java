import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[] dx = {0, -1, 0, 1};
	static int[] dy = {1, 0, -1, 0};
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		boolean[][] visited = new boolean[101][101];
		
		N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int y = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());
			
			visited[x][y] = true;
			
			int nx = x + dx[d];
			int ny = y + dy[d];
			visited[nx][ny] = true;
			x = nx;
			y = ny;
			
			List<Integer> dList = new ArrayList<>();
			dList.add(d);
			for (int j = 0; j < g; j++) {
				List<Integer> newDList = new ArrayList<>();
				for (int k = dList.size() - 1; k >= 0; k--) {
					d = (dList.get(k) + 1) % 4;
					nx = x + dx[d];
					ny = y + dy[d];
					visited[nx][ny] = true;
					x = nx;
					y = ny;
					newDList.add(d);
				}
				dList.addAll(newDList);
			}
			
		}
		
		bw.write(check(visited) + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
	
	static int check(boolean[][] visited) {
		int answer = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (visited[i][j] && visited[i][j+1]
						&& visited[i+1][j] && visited[i+1][j+1]) {
					answer++;
				}
			}
		}
		return answer;
	}
}
