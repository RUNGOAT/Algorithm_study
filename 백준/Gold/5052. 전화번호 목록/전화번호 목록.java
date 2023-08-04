import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static String[] numbers;
    
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            numbers = new String[N];
            for (int i = 0; i < N; i++) {
                numbers[i] = br.readLine();
            }
            
            sb.append(solution()).append("\n");
        }
        System.out.println(sb.toString());
    }
    
    static String solution() {
    	Arrays.sort(numbers);
    	
    	for (int i = 0; i < N-1; i++) {
    		if (numbers[i + 1].startsWith(numbers[i])) {
    			return "NO";
    		}
    	}
        return "YES";
    }
}