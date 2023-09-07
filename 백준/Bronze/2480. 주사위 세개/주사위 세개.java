import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
 
		int a, b, c;
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
 
		// 만약 모든 변수가 다른 경우
		if (a != b && b != c && a != c) {
			int max = Math.max(a, Math.max(b, c));
			System.out.println(max * 100);
		}
		// 3개의 변수가 모두 같은 경우
		else if (a == b && a == c) {
			System.out.println(10000 + a * 1000);
		}
		// a가 b혹은 c랑만 같은 경우
		else if(a == b || a == c) {
			System.out.println(1000 + a * 100);
		}
		// b가 c랑 같은 경우
		else {
			System.out.println(1000 + b * 100);
		}
	}
}