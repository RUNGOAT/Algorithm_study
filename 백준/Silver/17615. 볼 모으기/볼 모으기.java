import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static char[] line;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		line = br.readLine().toCharArray();
		int min = Integer.MAX_VALUE;
		
		min = Math.min(checkLeft('R', 0, N), min);
		min = Math.min(checkLeft('B', 0, N), min);
		min = Math.min(checkRight('R', 0, N), min);
		min = Math.min(checkRight('B', 0, N), min);
		
		System.out.println(min);
	}
	
	static int checkLeft(char target, int start, int end) {
		int res = 0, cnt = 0;
		for (int i = start; i < end; i ++) {
			if (line[i] != target) {
				cnt = 1;
			} else {
				res += cnt;
			}
		}
		return res;
	}
	
	static int checkRight(char target, int start, int end) {
		int res = 0, cnt = 0;
		for (int i = end - 1; i >= start; i--) {
			if (line[i] != target) {
				cnt = 1;
			} else {
				res += cnt;
			}
		}
		return res;
	}

}
