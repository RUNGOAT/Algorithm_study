import java.io.*;
import java.util.*;

class CCTV {
	int x, y, d;

	CCTV(int x, int y, int d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}
}

public class Main {

	static int N, M;
	static int[][] arr;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };
	static List<CCTV> list;
	static int[][] lookCount;
	static int answer = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		lookCount = new int[N][M];
		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		list = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] != 0 && arr[i][j] != 6) {
					list.add(new CCTV(i, j, arr[i][j]));
				}
			}
		}
		
		look(0);
		
		System.out.println(answer);
	}

	static void look(int idx) {
		if (idx == list.size()) {
			answer = Math.min(answer, checkMap());
			return;
		}
		
		CCTV cctv = list.get(idx);
		switch (cctv.d) {
		case 1:
			for (int d = 0; d < 4; d++) {
				move(cctv.x, cctv.y, d);
				look(idx + 1);
				revoke(cctv.x, cctv.y, d);
			}
			break;
			
		case 2:
			for (int d = 0; d < 2; d++) {
				move(cctv.x, cctv.y, d);
				move(cctv.x, cctv.y, (d + 2) % 4);
				look(idx + 1);
				revoke(cctv.x, cctv.y, d);
				revoke(cctv.x, cctv.y, (d + 2) % 4);
			}
			break;
		
		case 3:
			for (int d = 0; d < 4; d++) {
				move(cctv.x, cctv.y, d);
				move(cctv.x, cctv.y, (d + 1) % 4);
				look(idx + 1);
				revoke(cctv.x, cctv.y, d);
				revoke(cctv.x, cctv.y, (d + 1) % 4);
			}
			break;
			
		case 4:
			for (int d = 0; d < 4; d++) {
				move(cctv.x, cctv.y, d);
				move(cctv.x, cctv.y, (d + 1) % 4);
				move(cctv.x, cctv.y, (d + 2) % 4);
				look(idx + 1);
				revoke(cctv.x, cctv.y, d);
				revoke(cctv.x, cctv.y, (d + 1) % 4);
				revoke(cctv.x, cctv.y, (d + 2) % 4);
			}
			break;
			
		case 5:
			for (int d = 0; d < 4; d++) {
				move(cctv.x, cctv.y, d);
			}
			look(idx + 1);
			for (int d = 0; d < 4; d++) {
				revoke(cctv.x, cctv.y, d);
			}
			break;
		}
	}
	
	static void move(int x, int y, int d) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		while (!rangeOut(nx, ny)) {
			if (arr[nx][ny] == 0) {
				arr[nx][ny] = -1;				
			}
			lookCount[nx][ny]++;
			nx += dx[d];
			ny += dy[d]; 
		}
	}

	static void revoke(int x, int y, int d) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		while (!rangeOut(nx, ny)) {
			if (--lookCount[nx][ny] == 0) {
				if (arr[nx][ny] == -1) {
					arr[nx][ny] = 0;					
				}
			}
			nx += dx[d];
			ny += dy[d]; 
		}
	}
	
	static boolean rangeOut(int x, int y) {
		if (0 > x || N <= x || 0 > y || M <= y)
			return true;
		if (arr[x][y] == 6)	return true;
		return false;
	}
	
	static int checkMap() {
		int count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 0)	count++;
			}
		}
		return count;
	}
	
	static void print() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}
}
