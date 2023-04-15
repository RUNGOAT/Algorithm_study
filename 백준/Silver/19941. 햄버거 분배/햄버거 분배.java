import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, K;
	static char[] line;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		line = br.readLine().toCharArray();
		
		int answer = 0;
		for (int i = 0; i < N; i++) {
			if (line[i] == 'P' && isAte(i)) {
				answer++;
			}
		}
		
		System.out.println(answer);
		
	}
	
	static boolean isAte(int index) {
		int start = index - K < 0 ? 0 : index - K;
		int end = index + K < N ? index + K : N-1;
		for (int i = start; i <= end; i++) {
			if (line[i] == 'H') {
				line[i] = 'X';
				return true;
			}
		}
		return false;
	}
	
}
