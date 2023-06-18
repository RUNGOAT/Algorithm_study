import java.util.*;
import java.io.*;

public class Main {
	
	static int N;
	static int answer = 0;
	static int[] arr;
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        
        nQueen(0);
        System.out.println(answer);
    }
    
    static void nQueen(int depth) {
    	if (depth == N) {
    		answer++;
    		return;
    	}
    	for (int i = 0; i < N; i++) {
    		arr[depth] = i;
    		if (possible(depth)) {
    			nQueen(depth + 1);
    		}
    	}
    }
    
    static boolean possible(int depth) {
    	for (int i = 0; i < depth; i++) {
    		if (arr[depth] == arr[i]) {
    			return false;
    		} else if ((depth - i) == Math.abs(arr[depth] - arr[i])) {
    			return false;
    		}
    	}
    	return true;
    }

}
