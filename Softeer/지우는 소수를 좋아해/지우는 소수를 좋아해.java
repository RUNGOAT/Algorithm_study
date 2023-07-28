import java.util.*;
import java.io.*;

class GYM implements Comparable<GYM> {
	int v, level;

	GYM(int v, int level) {
		this.v = v;
		this.level = level;
	}

	@Override
	public int compareTo(GYM o) {
		return Integer.compare(this.level, o.level);
	}
}

public class Main {
	static int N, M;
	static List<GYM>[] graph;
	static int[] dist;

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		graph = new ArrayList[N + 1];
		for (int i = 0; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			graph[a].add(new GYM(b, c));
			graph[b].add(new GYM(a, c));
		}

		dist = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			dist[i] = Integer.MAX_VALUE;
		}

		dijkstra(1);
		for (int num = dist[N] + 1;; num++) {
			if (num % 2 == 0) {
				continue;
			}
			boolean isPrimeNumber = true;
			for (int i = 2; i <= Math.sqrt(num); i++) {
				if (num % i == 0) {
					isPrimeNumber = false;
					break;
				}
			}
			if (isPrimeNumber) {
				System.out.println(num);
				break;
			}
		}
	}

	static void dijkstra(int v) {
		PriorityQueue<GYM> pq = new PriorityQueue();
		pq.add(new GYM(v, 0));
		dist[v] = 0;
		
		while (!pq.isEmpty()) {
			GYM cur = pq.poll();
			if (dist[cur.v] < cur.level) {
				continue;
			}
			for (GYM next : graph[cur.v]) {
				int nextDist = Math.max(cur.level, next.level);
				if (nextDist < dist[next.v]) {
					dist[next.v] = nextDist;
					pq.add(new GYM(next.v, nextDist));
				}
			}
		}
	}

}
