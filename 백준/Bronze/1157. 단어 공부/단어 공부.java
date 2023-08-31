import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String line = br.readLine().toUpperCase();
		int[] cnt = new int[26];
		
		for (int i = 0; i < line.length(); i++) {
			cnt[line.charAt(i) - 'A']++;
		}
		
		int max = 0;
		for (int i = 0; i < 26; i++) {
			max = Math.max(max, cnt[i]);
		}
		
		
		char answer = 'A';
		boolean onlyOne = false;
		for (int i = 0; i < 26; i++) {
			if (max == cnt[i]) {
				if (onlyOne) {
					answer = '?';
					break;
				}
				answer += i;
				onlyOne = true;
			}
		}
		
		bw.write(answer + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}
