import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {
	int v, w;

	public Edge(int v, int w) {
		super();
		this.v = v;
		this.w = w;
	}

	@Override
	public int compareTo(Edge o) {
		return this.w - o.w;
	}
}

public class Main {
	
	static int V, E, K;
	static ArrayList<Edge>[] adjL;
	static int[] dist;
	static PriorityQueue<Edge> pq;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(br.readLine());
		
		adjL = new ArrayList[V+1];
		for (int i = 1; i <= V; i++)
			adjL[i] = new ArrayList<Edge>();
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjL[u].add(new Edge(v, w));
		}
		
		dist = new int[V+1];
		
		Arrays.fill(dist, Integer.MAX_VALUE);
		
		dist[K] = 0;
		
		dijkstra(K);
		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= V; i++) {
			if (dist[i] == Integer.MAX_VALUE) {
				sb.append("INF").append("\n");
				continue;
			}
			sb.append(dist[i]).append("\n");
		}
		System.out.println(sb);
	}
	
	static void dijkstra(int v) {
		pq = new PriorityQueue<Edge>();
		pq.add(new Edge(v, 0));
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			for (Edge next : adjL[now.v]) {
				if (dist[next.v]> now.w + next.w) {
					dist[next.v] = now.w + next.w;
					pq.add(new Edge(next.v, dist[next.v]));
				}
			}
		}
	}
}
