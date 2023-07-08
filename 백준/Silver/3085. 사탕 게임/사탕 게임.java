import java.util.*;
import java.io.*;

public class Main {
	
	static int N;
	static char[][] grid;
	static boolean[][] visited;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int answer = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		grid = new char[N][N];
		for (int i = 0; i < N; i++) {
			grid[i] = br.readLine().toCharArray();
		}
		
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				changeCandy(i, j);
			}
		}
		System.out.println(answer);
	}
	
	static void changeCandy(int x, int y) {
		
		visited[x][y] = true;
		
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (0 > nx || N <= nx || 0 > ny || N <= ny)
				continue;
			if (visited[nx][ny])			continue;
			if (grid[nx][ny] == grid[x][y])	continue;
			swap(x, y, nx, ny);
			updateAnswer();
			swap(nx, ny, x, y);
		}
	}
	
	static void swap(int x, int y, int nx, int ny) {
		char temp = grid[x][y];
		grid[x][y] = grid[nx][ny];
		grid[nx][ny] = temp;
	}
	
	static void updateAnswer() {
		for (int i = 0; i < N; i++) {
			getMax(i, true);
			getMax(i, false);
		}
	}
	
	static void getMax(int idx, boolean isRow) {
		int count = 1;
		char firstChar = isRow ? grid[idx][0] : grid[0][idx];
		for (int j = 1; j < N; j++) {
			char curChar = isRow ? grid[idx][j] : grid[j][idx];
			if (curChar != firstChar) {
				if (count > answer) {
					answer = count;
				}
				firstChar = curChar;
				count = 1;
			} else {
				count++;
			}
		}
		if (count > answer) {
			answer = count;
		}
	}
}