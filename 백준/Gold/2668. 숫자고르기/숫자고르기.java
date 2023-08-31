import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Main {
	

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N+1];
		for (int i = 1; i <= N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Set<Integer> answer = new TreeSet<>();
		for (int i = 1; i <= N; i++) {
			boolean[] visited = new boolean[N+1];
			int j = i;
			List<Integer> list = new ArrayList<>();
			while (!visited[j]) {
				list.add(j);
				visited[j] = true;
				j = arr[j];
				if (j == i) {
					answer.addAll(list);
				}
			}
		}
		
		bw.write(answer.size() + "\n");
		for (int i : answer) {
			bw.write(i + "\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}
}
