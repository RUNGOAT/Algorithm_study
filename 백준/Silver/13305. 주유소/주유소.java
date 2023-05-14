import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] length = new int[N-1];
		for (int i = 0; i < N-1; i++) {
			length[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		int[] cities = new int[N];
		for (int i = 0; i < N; i++) {
			cities[i] = Integer.parseInt(st.nextToken());
		}
		
		long answer = 0;
		int oil = cities[0];
		for (int i = 0; i < N-1; i++) {
			oil = cities[i] > oil ? oil : cities[i];
			answer += oil * length[i];
		}
		
		System.out.println(answer);
		
	}

}
