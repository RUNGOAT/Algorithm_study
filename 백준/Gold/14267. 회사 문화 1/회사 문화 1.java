import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Main {

	static int N, M;
	static ArrayList<Integer>[] employees;
	static int[] praises;
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		employees = new ArrayList[N+1];
		for (int i = 1; i <= N; i++) {
			employees[i] = new ArrayList<>();
		}
		st = new StringTokenizer(br.readLine(), " ");
		st.nextToken();
		for (int i = 2; i <= N; i++) {
			int superior = Integer.parseInt(st.nextToken());
			employees[superior].add(i);
		}
		
		praises = new int[N+1]; 
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine(), " ");
			int i = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			praises[i] += w;
		}
		
		dfs(1);
		
		for (int i = 1; i <= N; i++) {
			bw.write(praises[i] + " ");
		}
		bw.write("\n");
		
		bw.flush();
		bw.close();
		br.close();
	}
	
	static void dfs(int cur) {
		for (int next : employees[cur]) {
			praises[next] += praises[cur];
			dfs(next);
		}
	}
	
}