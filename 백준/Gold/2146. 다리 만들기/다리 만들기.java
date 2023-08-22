import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

class Node {
	int x, y;
	int dist;
	
	public Node(int x, int y, int dist) {
		this.x = x;
		this.y = y;
		this.dist = dist;
	}
}

public class Main
{
	static int N;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int answer = Integer.MAX_VALUE;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st;
    	N = Integer.parseInt(br.readLine());
    	map = new int[N][N];
    	
    	for (int i = 0; i < N; i++) {
    		st = new StringTokenizer(br.readLine(), " ");
    		for (int j = 0; j < N; j++) {
    			map[i][j] = Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	List<Set<Node>> allSet = new ArrayList<>();
    	
    	int cnt = 2;
    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < N; j++) {
    			if (map[i][j] == 1) {
    				// 육지의 바다 인접 지점 리스트 모음
    				allSet.add(setNum(i, j, cnt++));
    			}
    		}
    	}
    	
    	int num = 2;
    	for (int i = 0; i < allSet.size(); i++) {
    		Set<Node> set = allSet.get(i);
    		Queue<Node> q = new LinkedList<>();
    		visited = new boolean[N][N];
    		for (Node node : set) {
    			q.offer(node);
    			visited[node.x][node.y] = true; 
    		}
    		bfs(q, visited, num++);
    	}

    	bw.write(answer + "\n");
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static void bfs(Queue<Node> q, boolean[][] visited, int num) {
    	
    	while (!q.isEmpty()) {
    		Node cur = q.poll();
    		if (answer < cur.dist)
    			continue;
    		
    		for (int d = 0; d < 4; d++) {
    			int nx = cur.x + dx[d];
    			int ny = cur.y + dy[d];
    			if (rangeOut(nx, ny))	continue;
    			if (visited[nx][ny])	continue;
    			if (map[nx][ny] == num)	continue;
    			if (map[nx][ny] != 0) {
    				answer = Math.min(answer, cur.dist);
    			} else {
    				q.offer(new Node(nx, ny, cur.dist + 1));
    				visited[nx][ny] = true;
    			}
    		}
    	}
    }
    
    static Set<Node> setNum(int x, int y, int cnt) {
    	Set<Node> set = new HashSet<>();
    	Queue<Node> q = new LinkedList<>();
    	q.add(new Node(x, y, 0));
    	map[x][y] = cnt;
    	
    	while (!q.isEmpty()) {
    		Node cur = q.poll();
    		
    		for (int d = 0; d < 4; d++) {
    			int nx = cur.x + dx[d];
    			int ny = cur.y + dy[d];
    			if (rangeOut(nx, ny))	continue;
    			if (map[nx][ny] == 0) {
    				set.add(new Node(cur.x, cur.y, 0));
    			} else if (map[nx][ny] == 1) {
    				q.add(new Node(nx, ny, 0));
    				map[nx][ny] = cnt;
    			}
    		}
    	}
    	
    	return set;
    }
    
    static boolean rangeOut(int x, int y) {
    	return 0 > x || N <= x || 0 > y || N <= y;
    }
}
