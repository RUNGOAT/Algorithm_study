import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static int count(String[] arr, String v) {
		int cnt = 0;
		for (String ar : arr) {
			if (ar.equals(v)) cnt++;
		}
		return cnt;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split(" ");
		String v = br.readLine();
		System.out.println(count(arr, v));
		br.close();
	}

}
