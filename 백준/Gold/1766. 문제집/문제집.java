import java.util.*;
import java.io.*;

public class Main {
	
	static int N, M;
	static List<Integer>[] adjL;
	static int[] indegree;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		adjL = new ArrayList[N+1];
		for (int i = 0; i <= N; i++) {
			adjL[i] = new ArrayList<>();
		}
		indegree = new int[N+1];
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			adjL[a].add(b);
			indegree[b]++;
		}
		
		topologicalSort();
		
		System.out.println(sb.toString());
	}
	
	static void topologicalSort() {
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		
		for (int i = 1; i <= N; i++) {
			if (indegree[i] == 0) {
				pq.offer(i);
			}
		}
		
		while (!pq.isEmpty()) {
			int next = pq.poll();
			
			for (int i : adjL[next]) {
				indegree[i]--;
				
				if (indegree[i] == 0) {
					pq.offer(i);
				}
			}
			
			sb.append(next + " ");
		}
	}
}