import java.util.*;
import java.io.*;

class Point implements Comparable<Point> {
	int x, y, breakWall;
	Point(int x, int y, int breakWall) {
		this.x = x;
		this.y = y;
		this.breakWall = breakWall;
	}
	
	@Override
	public int compareTo(Point o) {
		return Integer.compare(this.breakWall, o.breakWall);
	}
}

public class Main {

	static int M, N;
	static char[][] maze;
	static int[][] dist;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int answer = Integer.MAX_VALUE;
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		
		maze = new char[N][M];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < M; j++) {
				maze[i][j] = line.charAt(j);
			}
		}
		
		dist = new int[N][M];
		// 벽을 부수지 않고 들어가기
		// 벽을 부수고 들어가기
		// 부순 벽의 갯수 체크
		bfs();
		bw.write(answer + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
	
	static void bfs() {
		PriorityQueue<Point> pq = new PriorityQueue<>();
		pq.add(new Point(0, 0, 0));
		for (int i = 0; i < N; i++) {
			Arrays.fill(dist[i], Integer.MAX_VALUE);			
		}
		
		while (!pq.isEmpty()) {
			Point cur = pq.poll();
			if (cur.x == N-1 && cur.y == M-1) {
				answer = Math.min(answer, cur.breakWall);
				continue;
			}
			
			for (int d = 0; d < 4; d++) {
				int nx = cur.x + dx[d];
				int ny = cur.y + dy[d];
				if (0 > nx || N <= nx || 0 > ny || M <= ny)	continue;
				if (dist[nx][ny] <= cur.breakWall) continue;

				dist[nx][ny] = cur.breakWall;
				if (maze[nx][ny] == '1') {
					pq.add(new Point(nx, ny, cur.breakWall + 1));
				} else {
					pq.add(new Point(nx, ny, cur.breakWall));
				}
			}
		}
	}
}