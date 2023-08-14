import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main
{
	static int N, M;
	static int[][] adjM;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	N = Integer.parseInt(br.readLine());
    	M = Integer.parseInt(br.readLine());
    	adjM = new int[N+1][N+1];
    	
    	for (int i = 1; i <= N; i++) {
    		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    		for (int j = 1; j <= N; j++) {
    			adjM[i][j] = Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	int[] travel = new int[M];
    	for (int i = 0; i < M; i++) {
    		travel[i] = Integer.parseInt(st.nextToken());
    	}
    	
    	boolean isNo = false;
    	for (int i = 1; i < M; i++) {
    		if (travel[i-1] == travel[i])	continue;
    		if (!bfs(travel[i-1], travel[i])) {
    			bw.write("NO\n");
    			isNo = true;
    			break;
    		}
    	}
    	if (!isNo)
    		bw.write("YES\n");
    	
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static boolean bfs(int cur, int target) {
    	Queue<Integer> q = new LinkedList<>();
    	q.offer(cur);
    	boolean[] visited = new boolean[N+1];
    	visited[cur] = true;
    	
    	while (!q.isEmpty()) {
    		int curr = q.poll();
    		if (curr == target) {
    			return true;
    		}
    		for (int i = 1; i <= N; i++) {
    			if (visited[i])	continue;
    			if (adjM[curr][i] == 1) {
    				q.offer(i);
    				visited[i] = true;
    			}
    		}
    	}
    	return false;
    }
}