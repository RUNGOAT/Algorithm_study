import java.util.*;
import java.io.*;

public class Main {
	
	static int[] arr;

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Stack<Integer> stack = new Stack<>();
		stack.push(arr[0]);
		
		for (int i = 1; i < N; i++) {
			int number = arr[i];
			
			if (stack.peek() < number) {
				stack.push(number);
			} else {
				int start = 0;
				int end = stack.size();
				while (start < end) {
					int mid = (start + end) / 2;
					if (stack.get(mid) < number) {
						start = mid + 1;
					} else {
						end = mid;
					}
				}
				stack.set(end, number);
			}
		}
		System.out.println(stack.size());
	}
}