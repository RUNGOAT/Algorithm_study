import java.util.*;
import java.io.*;

public class Main {
    static List<Integer>[] adjList;
    static boolean[] visited;
    static int[] depth;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        adjList = new ArrayList[N+1];
        for(int i=0; i<=N; i++){
            adjList[i] = new ArrayList<>();
        }

        visited = new boolean[N+1];
        depth = new int[N+1];

        int M = Integer.parseInt(br.readLine());
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            adjList[x].add(y);
            adjList[y].add(x);
        }

        bfs(X);

        if(visited[Y]){
            System.out.println(depth[Y]);
        } else {
            System.out.println("-1");
        }
    }

    public static void bfs(int x) {
        Queue<Integer> queue = new LinkedList<>();
        visited[x] = true;
        queue.add(x);

        while(!queue.isEmpty()){
            int curX = queue.poll();
            for(int i : adjList[curX]){
                if(!visited[i]){
                    visited[i] = true;
                    depth[i] = depth[curX] + 1;
                    queue.add(i);
                }
            }
        }
    }
}
