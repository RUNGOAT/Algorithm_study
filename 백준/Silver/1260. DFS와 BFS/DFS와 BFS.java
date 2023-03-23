import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
        static int[][] adjM;
        static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        adjM = new int[N+1][N+1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adjM[a][b] = 1;
            adjM[b][a] = 1;
        }

        visited = new boolean[N + 1];
        dfs(V);
        System.out.println();

        visited = new boolean[N + 1];
        bfs(V);
    }

    public static void dfs(int V) {
        visited[V] = true;
        System.out.print(V + " ");

        if (V == adjM.length) {
            return;
        }
        for (int j = 1; j < adjM.length; j++) {
            if (adjM[V][j] == 1 && !visited[j]) {
                dfs(j);
            }
        }
    }

    public static void bfs(int V) {
        Queue<Integer> que = new LinkedList<Integer>();

        que.add(V);
        visited[V] = true;
        System.out.print(V + " ");

        while (!que.isEmpty()) {
            int temp = que.poll();
            for (int i = 1; i < adjM.length; i++) {
                if (adjM[temp][i] == 1 && !visited[i]) {
                    que.add(i);
                    visited[i] = true;
                    System.out.print(i + " ");
                }
            }
        }
    }

}