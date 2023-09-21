import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static List<Integer>[] adjL;
	static boolean[] visited;
	static int answer;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        adjL = new ArrayList[N];
        for (int i = 0; i < N; i++) {
        	adjL[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	adjL[a].add(b);
        	adjL[b].add(a);
        }
        
        answer = 0;
        for (int i = 0; i < N; i++) {
        	visited = new boolean[N];
        	dfs(i, 1);
        	if (answer == 1) {
        		break;
        	}
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
    
    static void dfs(int idx, int depth) {
    	if (depth == 5) {
    		answer = 1;
    		return;
    	}
    	
    	visited[idx] = true;
    	for (int next : adjL[idx]) {
    		if (!visited[next]) {
    			dfs(next, depth+1);
    		}
    	}
    	visited[idx] = false;
    }
}
