import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static String S;
	static StringBuilder T;
	static int answer;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		S = br.readLine();
		T = new StringBuilder(br.readLine());
		dfs();
		System.out.println(answer);
	}
	
	static void dfs() {
		if (answer == 1) {
			return;
		}
		
		if (T.length() == S.length()) {
			if (T.toString().equals(S)) {
				answer = 1;
			}
			return;
		}
		
		if (T.charAt(T.length() - 1) == 'A') {
			T.deleteCharAt(T.length() - 1);
			dfs();
			T.append('A');
		}
		
		if (T.charAt(0) == 'B') {
			T.reverse();
			T.deleteCharAt(T.length() - 1);
			dfs();
			T.append('B');
			T.reverse();
		}
		
	}
	
}
