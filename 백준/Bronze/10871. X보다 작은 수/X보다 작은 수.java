import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		String[] arr = br.readLine().split(" ");
		for (String ar : arr) {
			if (X > Integer.parseInt(ar)) {
				sb.append(ar + " ");
			}
		}
		System.out.println(sb);
		br.close();
	}

}
