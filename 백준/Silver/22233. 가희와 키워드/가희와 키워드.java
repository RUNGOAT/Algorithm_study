import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Map<String, Boolean> map = new HashMap<>();
		for (int i = 0; i < N; i++) {
			map.put(br.readLine(), true);
		}
		
		for (int i = 0; i < M; i++) {
			String[] keywords = br.readLine().split(",");
			for (int j = 0; j < keywords.length; j++) {
				if (map.get(keywords[j]) != null) {
					map.remove(keywords[j]);
				}
			}
			System.out.println(map.size());
		}

	}

}
