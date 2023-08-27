import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
	int x, y;
	
	public Node(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	
	static int N, M;
	static char[][] map;
	static int answer = 0;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new char[N][M];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < M; j++) {
				map[i][j] = line.charAt(j);
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 'L') {
					bfs(i, j);
				}
			}
		}
		
		bw.write(answer + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
	
	static void bfs(int x, int y) {
		Queue<Node> q = new LinkedList<>();
		q.offer(new Node(x, y));
		int[][] visited = new int[N][M];
		visited[x][y] = 1;
		
		while (!q.isEmpty()) {
			Node cur = q.poll();
			answer = Math.max(answer, visited[cur.x][cur.y] - 1);
			
			for (int d = 0; d < 4; d++) {
				int nx = cur.x + dx[d];
				int ny = cur.y + dy[d];
				
				if (0 > nx || N <= nx || 0 > ny || M <= ny)	continue;
				if (map[nx][ny] != 'L')		continue;
				if (visited[nx][ny] != 0)	continue;
				visited[nx][ny] = visited[cur.x][cur.y] + 1;
				q.offer(new Node(nx, ny));
			}
		}
	}
}
