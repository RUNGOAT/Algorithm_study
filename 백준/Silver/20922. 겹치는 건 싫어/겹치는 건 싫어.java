import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] count = new int[100001];
		int start = 0, end = 0;
		int ans = 0;
		while (start < N) {
			while (end < N && count[arr[end]] < K) {
				count[arr[end]]++;
				end++;
			}
			
			int size = end - start;
			ans = Math.max(ans, size);
			count[arr[start]]--;
			start++;
		}
		System.out.println(ans);
	}

}
