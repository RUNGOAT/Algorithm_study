import java.io.*;
import java.util.*;

public class Main {

	static int N;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		
		int answer = 0;
		for (int i = 0; i < N; i++) {
			answer += twoPointer(i);
		}
		System.out.println(answer);
	}
	
	static int twoPointer(int key) {
		int target = arr[key];
		
		int i = 0, j = N-1;
		while (i < j) {
			if (i == key) {
				i++;
				continue;
			} else if (j == key) {
				j--;
				continue;
			}
			
			int result = arr[i] + arr[j];
			if (result == target) {
				return 1;
			} else if (result < target) {
				i++;
			} else {
				j--;
			}
		}
		return 0;
	}
}
