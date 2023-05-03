import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int min = Integer.MAX_VALUE;
		
		int aCnt = 0;
		for (int i = 0; i < line.length(); i++) {
			if (line.charAt(i) == 'a')
				aCnt++;
		}
		
		for (int i = 0; i < line.length(); i++) {
			int bCnt = 0;
			for (int j = i; j < i + aCnt; j++) {
				if (line.charAt(j % line.length()) =='b')
					bCnt++;
			}
			min = Math.min(min, bCnt);
		}
		System.out.println(min);
	}

}
