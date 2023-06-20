import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;


public class Main {
	
	static List<String>[] list = new ArrayList[11];
	static int[] dp = new int[11];
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	int n = Integer.parseInt(st.nextToken());
    	int k = Integer.parseInt(st.nextToken());
    	br.close();
    	
    	list[1] = new ArrayList<>(Collections.singletonList("1"));
        list[2] = new ArrayList<>(Arrays.asList("11", "2"));
        list[3] = new ArrayList<>(Arrays.asList("111", "12", "21", "3"));
    	
    	dp[1] = 1;
    	dp[2] = 2;
    	dp[3] = 4;
    	
    	for (int i = 4; i < 11; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
            list[i] = new ArrayList<>();
            makeNumberSum("1", i - 1, i);
            makeNumberSum("2", i - 2, i);
            makeNumberSum("3", i - 3, i);
        }

        if (k > dp[n]) {
            System.out.println(-1);
            System.exit(0);
        }

        System.out.println(String.join("+", list[n].get(k - 1).split("")));
    	
    }
    
    static void makeNumberSum(String i, int key, int number) {
    	for (String num : list[key]) {
    		list[number].add(i + num);
    	}
    }
}
