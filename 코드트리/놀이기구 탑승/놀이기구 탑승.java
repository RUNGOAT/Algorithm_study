import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	static int n;
	static int[][] arr;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		Map<Integer, int[]> map = new HashMap<>();
		int[] score = { 0, 1, 10, 100, 1000 };

		for (int x = 0; x < n * n; x++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int student = Integer.parseInt(st.nextToken());
			int[] likeStudent = { Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
					Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()) };

			map.put(student, likeStudent);
			ride(student, likeStudent);
		}

		int answer = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int[] likeBlank = likeBlankCheck(i, j, map.get(arr[i][j]));
				answer += score[likeBlank[0]];
			}
		}
		System.out.println(answer);
	}

	static void ride(int student, int[] likeStudent) {
		int maxFriend = 0, maxBlank = 0;
		int r = 0, c = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (arr[i][j] == 0) {
					int[] likeBlank = likeBlankCheck(i, j, likeStudent);
					int[] result = check(r, c, i, j, maxFriend, maxBlank, likeBlank);
					r = result[0];
					c = result[1];
					maxFriend = result[2];
					maxBlank = result[3];
				}
			}
		}
		arr[r][c] = student;
	}

	private static int[] check(int r, int c, int i, int j, int maxFriend, int maxBlank, int[] likeBlank) {
		// 1. 좋아하는 친구 많은 위치
		if (maxFriend < likeBlank[0]) {
			maxFriend = likeBlank[0];
			maxBlank = likeBlank[1];
			r = i;
			c = j;
		} else if (maxFriend == likeBlank[0]) {
			// 2. 빈 칸이 많은 위치
			if (maxBlank < likeBlank[1]) {
				maxBlank = likeBlank[1];
				r = i;
				c = j;
			} else if (maxBlank == likeBlank[1]) {
				// 3. 행 번호가 작은 위치
				if (r < i) {
					r = i;
					c = j;
				} else if (r == i) {
					// 4. 열 번호가 작은 위치
					if (c < j) {
						c = j;
					}
				}
			}
		}
		return new int[] { r, c, maxFriend, maxBlank };
	}

	static int[] likeBlankCheck(int x, int y, int[] friends) {
		int friend = 0;
		int blank = 0;
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (0 > nx || n <= nx || 0 > ny || n <= ny)
				continue;
			if (arr[nx][ny] == 0)
				// 빈 칸인 경우
				blank++;
			else if (likeIn(friends, arr[nx][ny]))
				// 좋아하는 친구인 경우
				friend++;
		}
		return new int[] { friend, blank };
	}

	static boolean likeIn(int[] friends, int friend) {
		for (int number : friends) {
			if (number == friend)
				return true;
		}
		return false;
	}

}
