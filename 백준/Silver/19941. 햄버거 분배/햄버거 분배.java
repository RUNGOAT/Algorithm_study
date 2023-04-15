import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		boolean[] isAte = new boolean[N];
		String str = br.readLine();
		
		int answer = 0;
		for (int i = 0; i < N; i++) {
			if (str.charAt(i) == 'P') {
				boolean leftAte = false;
				for (int k = K; k > 0; k--) {
					if (i < k)	continue;
					if (str.charAt(i - k) == 'P') continue;
					if (isAte[i - k])	continue;
					isAte[i - k] = true;
					answer++;
					leftAte = true;
					break;
				}
				if (!leftAte) {
					for (int k = 1; k <= K; k++) {
						if (i + k >= N)	continue;
						if (str.charAt(i + k) == 'P') continue;
						if (isAte[i + k])	continue;
						isAte[i + k] = true;
						answer++;
						break;
					}
				}
			}
		}
		
		System.out.println(answer);
		
	}
	
}
