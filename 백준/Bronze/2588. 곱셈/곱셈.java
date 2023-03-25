import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int A = Integer.parseInt(br.readLine());
		String b = br.readLine();
		char[] B = b.toCharArray();
		System.out.println(A * Character.getNumericValue(B[2]));
		System.out.println(A * Character.getNumericValue(B[1]));
		System.out.println(A * Character.getNumericValue(B[0]));
		System.out.println(A * Integer.parseInt(b));
	}
}
