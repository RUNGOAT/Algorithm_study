import java.util.*;
import java.io.*;

public class Main {
	
	static int N;
	static List<Integer>[] adjL;
	static int Y;

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	N = Integer.parseInt(br.readLine());
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	int X = Integer.parseInt(st.nextToken());
    	Y = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(br.readLine());
    	
    	adjL = new ArrayList[N+1];
    	for (int i = 0; i <= N; i++) {
    		adjL[i] = new ArrayList<>();
    	}
    	
    	for (int i = 0; i < M; i++) {
    		st = new StringTokenizer(br.readLine());
    		int x = Integer.parseInt(st.nextToken());
    		int y = Integer.parseInt(st.nextToken());
    		
    		adjL[x].add(y);
    		adjL[y].add(x);
    	}
    	
    	System.out.println(bfs(X, Y));
    }
    
    static int bfs(int x, int y) {
    	Queue<Integer> q = new LinkedList<>();
    	q.add(x);
    	int[] visited = new int[N+1];
    	visited[x] = 1;
    	while (!q.isEmpty()) {
    		int curX = q.poll();
    		for (int next : adjL[curX]) {
    			if (visited[next] != 0)	continue;
				if (next == Y) {
					return visited[curX];
				}
				q.add(next);
				visited[next] = visited[curX] + 1;
    		}
    	}
    	return -1;
    }
}