import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int V, E;
	static List<Integer>[] adjL;
	static boolean[] visited;

	static void dfs(int v) {
		visited[v] = true;
		for (int w : adjL[v]) {
			if (!visited[w])
				dfs(w);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		V = Integer.parseInt(br.readLine());
		E = Integer.parseInt(br.readLine());
		adjL = new ArrayList[V + 1];
		visited = new boolean[V + 1];

		for (int i = 1; i <= V; i++) {
			adjL[i] = new ArrayList<>();
			visited[i] = false;
		}

		for (int i = 0; i < E; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			adjL[a].add(b);
			adjL[b].add(a);
		}

		dfs(1);

		int cnt = 0;
		for (int i = 2; i <= V; i++) {
			if (visited[i])
				cnt++;
		}
		System.out.println(cnt);
	}
}
