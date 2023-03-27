import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	
	static int binarySearch(int key, int[] arr) {
		int mid;
		int start = 0;
		int end = arr.length - 1;
				
		while (start <= end) {
			mid = (start + end) / 2;
			
			if (key == arr[mid])
				return 1;
			else if (key < arr[mid])
				end = mid - 1;
			else
				start = mid + 1;
		}
		
		return 0;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < M; i++) {
			int key = Integer.parseInt(st.nextToken());
			System.out.println(binarySearch(key, arr));
		}
	}
}
