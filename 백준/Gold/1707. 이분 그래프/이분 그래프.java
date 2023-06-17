import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer>[] adjList;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        for(int test = 0; test < K; test++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            adjList = new ArrayList[V+1];
            for (int i = 1; i <= V; i++) {
                adjList[i] = new ArrayList<>();
            }

            visited = new int[V+1];

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                adjList[u].add(v);
                adjList[v].add(u);
            }

            boolean result = true;
            for (int i = 1; i <= V; i++) {
                if (visited[i] == 0) {
                    if (!bfs(i)) {
                        result = false;
                        break;
                    }
                }
            }
            System.out.println(result ? "YES" : "NO");
        }
    }

    static boolean bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = 1;

        while (!q.isEmpty()) {
            int v = q.poll();

            for (int w : adjList[v]) {
                if (visited[w] == 0) {
                    visited[w] = -1 * visited[v];
                    q.add(w);
                } else if (visited[w] == visited[v]) {
                    return false;
                }
            }
        }
        return true;
    }
}
