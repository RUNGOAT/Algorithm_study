import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[N+1];
        for (int i = 1; i <= N; i++) {
        	arr[i] = i;
        }
        
        for (int m = 0; m < M; m++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	int i = Integer.parseInt(st.nextToken());
        	int j = Integer.parseInt(st.nextToken());
        	change(i, j, arr);
        }
        
        for (int i = 1; i <= N; i++) {
        	bw.write(arr[i] + " ");
        }
        bw.write("\n");
        
        bw.flush();
        bw.close();
        br.close();
    }
        
    static void change(int i, int j, int[] arr) {
    	int tmp = arr[i];
    	arr[i] = arr[j];
    	arr[j] = tmp;
    }
}
