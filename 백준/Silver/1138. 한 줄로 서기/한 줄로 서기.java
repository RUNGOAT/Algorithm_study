import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[] line = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			line[i] = Integer.parseInt(st.nextToken());
		}
		
		List<Integer> answer = new LinkedList<Integer>();
		for (int i = N-1; i >= 0; i--) {
			answer.add(line[i], i+1);
		}
		
		for (int n : answer) {
			System.out.print(n + " ");	
		}
	}
	
}
