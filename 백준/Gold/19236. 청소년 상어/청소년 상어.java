import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Fish {
	int num, dir;

	public Fish(int num, int dir) {
		super();
		this.num = num;
		this.dir = dir;
	}

}

public class Main {

	static int[] shark = { 0, 0 };
	static int[] dx = { -1, -1, 0, 1, 1, 1, 0, -1 };
	static int[] dy = { 0, -1, -1, -1, 0, 1, 1, 1 };
	static int ans = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Fish[][] arr = new Fish[4][4];
		for (int i = 0; i < 4; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++) {
				int num = Integer.parseInt(st.nextToken());
				int dir = Integer.parseInt(st.nextToken());
				arr[i][j] = new Fish(num, dir - 1);
			}
		}
		// 상어는 (0, 0)에 있는 물고기 먹고 시작
		sharkMove(0, 0, arr[0][0].num, arr);

		System.out.println(ans);

	}

	static void sharkMove(int sx, int sy, int fish, Fish[][] arr) {
		ans = Math.max(ans, fish);
		Fish ateFish = clone(arr[sx][sy]);
		arr[sx][sy] = null;
		fishMove(arr);

		int x = sx, y = sy;
		while (true) {
			// 먹은 물고기의 방향으로 이동
			int nx = x + dx[ateFish.dir];
			int ny = y + dy[ateFish.dir];

			// 범위를 벗어나거나 빈 칸은 갈 수 없다.
			if (0 > nx || 4 <= nx || 0 > ny || 4 <= ny)	break;
			if (arr[nx][ny] == null) {
				// 여러 개의 칸으로 이동
				x = nx;
				y = ny;
				continue;
			}

			// 물고기 발견!
			Fish eat = clone(arr[nx][ny]);
			shark = new int[] { nx, ny };
			sharkMove(nx, ny, fish + arr[nx][ny].num, copy(arr));
			shark = new int[] { sx, sy };
			arr[nx][ny] = clone(eat);

			// 여러 개의 칸으로 이동
			x = nx;
			y = ny;
		}

		if (x == sx && y == sy) {
			// 상어가 갈 곳이 없어 집으로 간다.
			return;
		}

	}

	// 물고기 번호가 작은 순부터 이동
	static void fishMove(Fish[][] arr) {
		int number = 1;
		while (number != 17) {
			findNumberEqualFish(number++, arr);
		}
	}

	static void findNumberEqualFish(int number, Fish[][] arr) {
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (arr[i][j] != null && arr[i][j].num == number) {
					// number에 해당하는 물고기 이동
					change(i, j, arr);
					return;
				}
			}
		}
	}

	// 갈 수 있는 칸 만날 때 까지 45도 반시계 회전 < 8번
	private static int[] fishMoveCheck(int x, int y, Fish[][] arr) {

		// 이동할 칸이 없는 경우도 존재
		int nx = x, ny = y;
		for (int i = 0; i < 8; i++) {
			nx = x + dx[(arr[x][y].dir + i) % 8];
			ny = y + dy[(arr[x][y].dir + i) % 8];
			if (0 > nx || 4 <= nx || 0 > ny || 4 <= ny)	continue;
			if (nx == shark[0] && ny == shark[1])	continue;
			arr[x][y].dir = (arr[x][y].dir + i) % 8;
			break;
		}

		return new int[] { nx, ny };

	}

	private static void change(int x, int y, Fish[][] arr) {
		// 물고기가 이동할 위치 반환
		int[] next = fishMoveCheck(x, y, arr);

		// 물고기가 이동하면 서로의 값 바꾼다.
		Fish change = arr[next[0]][next[1]];
		arr[next[0]][next[1]] = clone(arr[x][y]);
		arr[x][y] = change;
	}

	private static Fish[][] copy(Fish[][] fish) {
		Fish[][] copy = new Fish[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (fish[i][j] == null) {
					copy[i][j] = null;
					continue;
				}
				copy[i][j] = clone(fish[i][j]);
			}
		}
		return copy;
	}

	private static Fish clone(Fish fish) {
		return new Fish(fish.num, fish.dir);
	}

}
