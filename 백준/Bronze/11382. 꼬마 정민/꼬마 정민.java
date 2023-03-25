import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static long sum(String[] array) {
		long total = 0;
		for (String num : array) {
			total += Long.parseLong(num);
		}
		return total;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] ABC = br.readLine().split(" ");
		System.out.println(sum(ABC));
	}
	
}
