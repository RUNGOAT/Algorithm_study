import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main
{
	static int N;
	static int answer = 0;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	N = Integer.parseInt(br.readLine());
    	
    	solution();
    	
    	bw.write(answer + "\n");
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static void solution() {
    	List<Integer> primeList = new ArrayList<>();
    	int num = 0;
    	for (int i = 2; i <= N; i++) {
    		if (num + i > N) {
    			break;
    		}
    		boolean flag = true;
    		for (int j = 2; j <= Math.sqrt(i); j++) {
    			if (i % j == 0) {
    				flag = false;
    				break;
    			}
    		}
    		if (flag) {
    			num = i;
    			primeList.add(i);
    		}
    	}
    	
    	boolean flag = true;
		for (int j = 2; j <= Math.sqrt(N); j++) {
			if (N % j == 0) {
				flag = false;
				break;
			}
		}
		if (flag && N != 1) {
			primeList.add(N);
		}
    	
    	if (N == 2 || N == 3) {
    		answer = 1;
    		return;
    	}
    	int size = primeList.size();
    	int s = 0, e = 0;
    	int sum = 0;
    	while (true) {
    		if (sum < N) {
    			if (e >= size) {
    				return;
    			}
    			sum += primeList.get(e);
    			e++;
    		} else if (sum > N) {
    			sum -= primeList.get(s);
    			s++;
    		} else {
    			answer++;
    			if (e >= size) {
    				return;
    			}
    			sum += primeList.get(e);
    			e++;
    		}
    	}
    }
}
