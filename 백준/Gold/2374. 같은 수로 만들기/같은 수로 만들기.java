import java.util.*;
import java.io.*;

public class Main {
	
	static int N;
	static long answer;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		divide(arr, arr[getMaxIndex(arr)]);
		System.out.println(answer);
	}
	
	static void divide(int[] arr, int max) {
		if (arr.length == 0) {
			return;
		}
		if (arr.length == 1 || sameCheck(arr)) {
			answer += max - arr[0];
			return;
		}
		int maxIdx = getMaxIndex(arr);
		divide(Arrays.copyOfRange(arr, 0, maxIdx), arr[maxIdx]);
		
		if (maxIdx+1 < arr.length) {
			divide(Arrays.copyOfRange(arr, maxIdx+1, arr.length), arr[maxIdx]);
		}
		
		answer += max - arr[maxIdx];
	}
	
	static int getMaxIndex(int[] arr) {
		int max = 0;
		int index = 0;
		for (int i = 0; i < arr.length; i++) {
			if (max < arr[i]) {
				max = arr[i];
				index = i;
			}
		}
		return index;
	}
	
	static boolean sameCheck(int[] arr) {
		int first = arr[0];
		for (int i = 1; i < arr.length; i++) {
			if (first != arr[i]) {
				return false;
			}
		}
		return true;
	}
}