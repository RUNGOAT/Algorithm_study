import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
	int v, c;
	Node(int v, int c) {
		this.v = v;
		this.c = c;
	}
	
	@Override
	public int compareTo(Node o) {
		return Integer.compare(this.c, o.c);
	}
}

public class Main
{
	final static int INF = 200000000;
	static int N, E;
	static List<Node>[] graph;
	static int v1, v2;
	static int[] dist;
	static boolean[] visited;
	
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        
        graph = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
        	graph[i] = new ArrayList<>();
        }
        
        dist = new int[N+1];
        visited = new boolean[N+1];
        
        for (int i = 0; i < E; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	int c = Integer.parseInt(st.nextToken());
        	
        	graph[a].add(new Node(b, c));
        	graph[b].add(new Node(a, c));
        }
        
        st = new StringTokenizer(br.readLine(), " ");
        v1 = Integer.parseInt(st.nextToken());
        v2 = Integer.parseInt(st.nextToken());
        
        int answer1 = 0;
        answer1 += dijkstra(1, v1);
        answer1 += dijkstra(v1, v2);
        answer1 += dijkstra(v2, N);
        
        int answer2 = 0;
        answer2 += dijkstra(1, v2);
        answer2 += dijkstra(v2, v1);
        answer2 += dijkstra(v1, N);
        
        int answer = Math.min(answer1, answer2);
        if (answer >= INF) {
        	answer = -1;
        }
        
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
	}
    
    static int dijkstra(int start, int end) {
    	PriorityQueue<Node> pq = new PriorityQueue<>();
    	
    	Arrays.fill(dist, INF);
    	Arrays.fill(visited, false);
    	
    	dist[start] = 0;
    	pq.add(new Node(start, 0));
    	
    	while (!pq.isEmpty()) {
    		Node cur = pq.poll();
    		
    		if (visited[cur.v]) continue;
    		visited[cur.v] = true; 
    		for (Node next : graph[cur.v]) {
    			if (dist[next.v] > cur.c + next.c) {
    				dist[next.v] = cur.c + next.c;
    				pq.add(new Node(next.v, dist[next.v]));
    			}
    		}
    	}
    	return dist[end];
    }
}