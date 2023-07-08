import java.util.*;
import java.io.*;

public class Main {
	
	static int N;
	static char[][] arr;
	static Map<Character, Integer> map = new HashMap<>();
	static boolean[][] visited;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int answer = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		map.put('C', 1);
		map.put('P', 1);
		map.put('Z', 1);
		map.put('Y', 1);
		
		N = Integer.parseInt(br.readLine());
		arr = new char[N][N];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = line.charAt(j);
			}
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
			if (arr[nx][ny] == arr[x][y])	continue;
			change(x, y, nx, ny);
			countMax();
			change(nx, ny, x, y);
		}
	}
	
	static void change(int x, int y, int nx, int ny) {
		char temp = arr[x][y];
		arr[x][y] = arr[nx][ny];
		arr[nx][ny] = temp;
	}
	
	static void countMax() {
		for (int i = 0; i < N; i++) {
			char firstChar = arr[i][0];
			int count = 1;
			for (int j = 1; j < N; j++) {
				if (arr[i][j] != firstChar) {
					if (count > answer) {
						answer = count;
					}
					firstChar = arr[i][j];
					count = 1;
				} else {
					count++;
				}
			}
			if (count > answer) {
				answer = count;
			}
		}
		for (int i = 0; i < N; i++) {
			char firstChar = arr[0][i];
			int count = 1;
			for (int j = 1; j < N; j++) {
				if (arr[j][i] != firstChar) {
					if (count > answer) {
						answer = count;
					}
					firstChar = arr[j][i];
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
}