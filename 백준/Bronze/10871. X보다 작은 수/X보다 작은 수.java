import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void check(String[] arr, int v) {
		for (String ar : arr) {
			if (v > Integer.parseInt(ar)) {
				System.out.print(ar + " ");
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		String[] arr = br.readLine().split(" ");
		check(arr, X);
		
		br.close();
	}

}
