import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static int n;
	public static int ans_max;
	public static int[] dx = {-1, 1, 0, 0};
	public static int[] dy = {0, 0, -1, 1};
	public static int[][] board;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		board= new int[n][n];
		StringTokenizer st = null;
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0;j<n;j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		ans_max = 0;
		permutation(new int[5], 0);
		System.out.println(ans_max);

	}
	
	public static void permutation(int[] arr, int depth) {
		if(depth == 5) {
			int[] arr_copy = arr.clone();
			int[][] map_copy = new int[n][n];
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					map_copy[i][j] = board[i][j];
				}
			}
			
			for(int i=0;i<5;i++) {
				int dir = arr_copy[i];
				if(dir == 0) {
					up(map_copy);
				} else if(dir == 1) {
					down(map_copy);
				} else if(dir == 2) {
					left(map_copy);
				} else {
					right(map_copy);
				}
				int max_value = 0;
				for(int p=0;p<n;p++) {
					for(int q=0;q<n;q++) {
						max_value = Math.max(max_value, map_copy[p][q]);
					}
				}
				ans_max = Math.max(ans_max, max_value);
			}


			return;
		}
		for(int i=0;i<4;i++) {
			arr[depth] = i;
			permutation(arr, depth+1);
		}
	}
	
	public static void up(int[][] map) {
		boolean[][] visited = new boolean[n][n];
		for(int j=0;j<n;j++) {
			while(true) {
				int cnt = 0;
				int x = 0;
				int nx = x + dx[1]; 
				while(true) {
					if(nx >= n) break;
					if(map[nx][j] != 0 && !visited[x][j] && !visited[nx][j] && map[nx][j] == map[x][j]) {
						
						map[x][j] += map[nx][j];
						visited[x][j] = true;
						map[nx][j] = 0;
						cnt++;
					} else if(map[x][j] == 0 && map[nx][j] != 0) {
							map[x][j] = map[nx][j];
							map[nx][j] = 0;
							visited[x][j] = visited[nx][j];
							visited[nx][j] = false;
							cnt++;
					}
					x = nx;
					nx += dx[1];
				}
				if(cnt == 0) {
					break;
				}
			}

		}

	}
	
	public static void down(int[][] map) {
		boolean[][] visited = new boolean[n][n];
		for(int j=0;j<n;j++) {
			while(true) {
				int cnt = 0;
				int x = n-1;
				int nx = x + dx[0]; 
				while(true) {
					if(nx < 0) break;
					if(map[nx][j] != 0 && !visited[x][j] && !visited[nx][j] && map[nx][j] == map[x][j]) {
						map[x][j] += map[nx][j];
						visited[x][j] = true;
						map[nx][j] = 0;
						cnt++;
					} else if(map[x][j] == 0 && map[nx][j] != 0) {
							map[x][j] = map[nx][j];
							map[nx][j] = 0;
							visited[x][j] = visited[nx][j];
							visited[nx][j] = false;
							cnt++;
					}
					x = nx;
					nx += dx[0];
				}
				if(cnt == 0) {
					break;
				}
			}
			

		}
	}
	
	public static void left(int[][] map) {
		boolean[][] visited = new boolean[n][n];
		for(int i=0;i<n;i++) {
			
			while(true) {
				int cnt = 0;
				int y = 0;
				int ny = y + dy[3]; 
				while(true) {
					if(ny >= n) break;
					if(map[i][ny] != 0 && !visited[i][y] && !visited[i][ny] && map[i][y] == map[i][ny]) {
						map[i][y] += map[i][ny];
						visited[i][y] = true;
						map[i][ny] = 0;
						cnt++;
					} else if(map[i][y] == 0 && map[i][ny] != 0) {
							map[i][y] = map[i][ny];
							map[i][ny] = 0;
							visited[i][y] = visited[i][ny];
							visited[i][ny] = false;
							cnt++;
					}
					y = ny;
					ny += dy[3];

				}
				if(cnt ==0) {
					break;
				}
				
			}

		}
	}
	
	public static void right(int[][] map) {
		boolean[][] visited = new boolean[n][n];
		for(int i=0;i<n;i++) {
			
			while(true) {
				int cnt = 0;
				int y = n-1;
				int ny = y + dy[2]; 
				while(true) {
					if(ny < 0) break;
					if(map[i][ny] != 0 && !visited[i][y] && !visited[i][ny] && map[i][y] == map[i][ny]) {
						map[i][y] += map[i][ny];
						visited[i][y] = true;
						map[i][ny] = 0;
						cnt++;
					} else if(map[i][y] == 0 && map[i][ny] != 0) {
							map[i][y] = map[i][ny];
							map[i][ny] = 0;
							visited[i][y] = visited[i][ny];
							visited[i][ny] = false;
							cnt++;
					}
					y = ny;
					ny += dy[2];

				}
				if(cnt ==0) {
					break;
				}
				
			}

		}
	}
	
	

}