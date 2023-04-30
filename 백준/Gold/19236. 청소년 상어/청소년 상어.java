import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Fish {
	int a, b;

	public Fish(int a, int b) {
		super();
		this.a = a;
		this.b = b;
	}

}

public class Main {
	
	static Fish fishCopy(Fish arr) {
		if (arr == null)
			return null;
		return new Fish(arr.a, arr.b);
	}

	static int[][] visited = new int[4][4];
	static int[] shark = { 0, 0 };
	static List<Fish> list = new ArrayList<>();
	static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
	static int ans = 0;
	
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Fish[][] arr = new Fish[4][4];
		for (int i = 0; i < 4; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++) {
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				arr[i][j] = new Fish(a, b - 1);
			}
		}
		
		dfs(0, 0, arr[0][0].a, arr);
		
		System.out.println(ans);
		
	}
	
	// 상어는 (0, 0)에 있는 물고기 먹고 시작
	static void dfs(int sx, int sy, int fish, Fish[][] arr) {
		ans = Math.max(ans, fish);
		Fish copy = new Fish(arr[sx][sy].a, arr[sx][sy].b);
		arr[sx][sy] = null;
		fishMove(arr);
		
		int x = sx, y = sy;
		while (true) {
			int nx = x + dx[copy.b];
			int ny = y + dy[copy.b];
			if (0 > nx || 4 <= nx || 0 > ny || 4 <= ny)	break;
			if (arr[nx][ny] == null) {
				x = nx;
				y = ny;
				continue;
			}
			Fish tmp = new Fish(arr[nx][ny].a, arr[nx][ny].b);
			shark = new int[]{nx, ny};
			dfs(nx, ny, fish + arr[nx][ny].a, copy(arr));
			shark = new int[]{sx, sy};
			arr[nx][ny] = new Fish(tmp.a, tmp.b);
			x = nx;
			y = ny;
		}
		if (x == sx && y == sy) {
			return;
		}
		
	}
	
	// 물고기 번호가 작은 순부터 이동
	// 이동 칸에 상어 있으면 못 감
	// 갈 수 있는 칸 만날 때 까지 45도 반시계 회전 < 8번
	// 다른 물고기가 있는 곳으로 이동하면 서로의 값 바꾼다.
	static void fishMove(Fish[][] arr) {
		int number = 1;
		while (number < 17) {
			findFish(number++, arr);
		}
	}
	
	static void findFish(int number, Fish[][] arr) {
		boolean flag = false;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (arr[i][j] != null && arr[i][j].a == number) {
					int[] next = check(i, j, arr);
					Fish n = arr[next[0]][next[1]];
					arr[next[0]][next[1]] = new Fish(arr[i][j].a, arr[i][j].b);
					arr[i][j] = n;
					flag = true;
					break;
				}
			}
			if (flag)	break;
		}
	}
	
	private static int[] check(int x, int y, Fish[][] arr) {
		int nx = x, ny = y;
		for (int i = 0; i < 8; i++) {
			nx = x + dx[(arr[x][y].b + i) % 8];
			ny = y + dy[(arr[x][y].b + i) % 8];
			if (0 > nx || 4 <= nx || 0 > ny || 4 <= ny)	continue;
			if (nx == shark[0] && ny == shark[1])	continue;
			arr[x][y].b = (arr[x][y].b + i) % 8;
			break;
		}
		
		return new int[] {nx, ny};
		
	}
	
	private static  Fish[][] copy(Fish[][] fish) {
		Fish[][] copy = new Fish[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (fish[i][j] == null) {
					copy[i][j] = null;
					continue;
				}
				copy[i][j] = new Fish(fish[i][j].a, fish[i][j].b);
			}
		}
		return copy;
	}

}

