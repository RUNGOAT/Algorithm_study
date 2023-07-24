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
		
		int left = 0, right = N-1;
		while (left < right) {
			if (left == key) {
				left++;
				continue;
			} else if (right == key) {
				right--;
				continue;
			}
			
			int sum = arr[left] + arr[right];
			if (sum == target) {
				return 1;
			} else if (sum < target) {
				left++;
			} else {
				right--;
			}
		}
		return 0;
	}
}
