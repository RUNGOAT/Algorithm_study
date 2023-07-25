import java.util.*;
import java.io.*;

public class Main
{

    static int N, M, S, T;

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new ArrayList[N+1];
        List<Integer>[] reverse = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
            reverse[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            reverse[y].add(x);
        }
        
        st = new StringTokenizer(br.readLine(), " ");
        S = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        boolean[] visited1 = new boolean[N+1];
        visited1[T] = true;
        dfs(S, visited1, graph);
        boolean[] visited2 = new boolean[N+1];
        dfs(S, visited2, reverse);
        boolean[] visited3 = new boolean[N+1];
        visited3[S] = true;
        dfs(T, visited3, graph);
        boolean[] visited4 = new boolean[N+1];
        dfs(T, visited4, reverse);

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            if (visited1[i] && visited2[i] && visited3[i] && visited4[i]) {
                answer++;
            }
        }
        System.out.println(answer - 2);
    }

    static void dfs(int v, boolean[] visited, List<Integer>[] graph) {
        if (visited[v]) {
            return;
        }
        visited[v] = true;
        for (int w : graph[v]) {
            dfs(w, visited, graph);
        }
    }
}
