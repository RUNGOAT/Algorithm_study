import java.util.*;
import java.io.*;

public class Main {
	
	static int[][] arr;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        
        arr = new int[N][M];
        for (int i = 0; i < N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j = 0; j < M; j++) {
        		arr[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        System.out.println(bfs(N, M));
    }
    
    static int bfs(int N, int M) {
    	Queue<int[]> q = new LinkedList<>();
    	boolean flag = true;
    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < M; j++) {
    			if (arr[i][j] == 1) {
    				q.add(new int[] {i, j});
    			} else if (arr[i][j] == 0) {
    				flag = false;
    			}
    		}
    	}
    	
    	if (flag) {
    		return 0;
    	}
    	
    	while (!q.isEmpty()) {
    		int[] node = q.poll();
    		for (int d = 0; d < 4; d++) {
    			int nx = node[0] + dx[d];
    			int ny = node[1] + dy[d];
    			if (0 > nx || nx >= N || 0 > ny || ny >= M) {
    				continue;
    			}
    			if (arr[nx][ny] != 0)	continue;
    			q.add(new int[] {nx, ny});
    			arr[nx][ny] = arr[node[0]][node[1]] + 1;
    		}
    	}
    	
    	int answer = -1;
    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < M; j++) {
    			if (arr[i][j] == 0) {
    				return -1;
    			}
    			if (answer < arr[i][j]) {
    				answer = arr[i][j];
    			}
    		}
    	}
    	return answer - 1;
    }
    
}
