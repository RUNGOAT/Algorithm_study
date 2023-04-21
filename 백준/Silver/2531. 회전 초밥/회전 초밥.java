import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken()); // 접시의 수
		int d = Integer.parseInt(st.nextToken()); // 초밥의 가짓수
		int k = Integer.parseInt(st.nextToken()); // 연속 먹는 접시 수
		int c = Integer.parseInt(st.nextToken()); // 쿠폰 번호

		int[] belt = new int[N];
		int[] sushi = new int[d + 1];

		for (int i = 0; i < N; i++) {
			belt[i] = Integer.parseInt(br.readLine());
		}

		sushi[c] += 1;
		for (int i = 0; i < k; i++) {
			sushi[belt[i]] += 1;
		}

		int answer = 0;
		for (int i = 1; i <= d; i++) {
			if (sushi[i] != 0) {
				answer++;
			}
		}

		int count = answer;
		for (int i = 0; i < N; i++) {
			sushi[belt[i]] -= 1;
			if (sushi[belt[i]] == 0) {
				count--;
			}
			sushi[belt[(i + k) % N]] += 1;
			if (sushi[belt[(i + k) % N]] == 1) {
				count++;
			}
			answer = Math.max(answer, count);
		}
		System.out.println(answer);
	}

}
