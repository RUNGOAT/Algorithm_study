import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int H = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		int[] line = new int[W];
		st = new StringTokenizer(br.readLine());
		int max = 0;
		List<Integer> list = new ArrayList<>();
		for (int i = 0; i < W; i++) {
			line[i] = Integer.parseInt(st.nextToken());
			if (max == line[i]) {
				list.add(i);
			} else if (max < line[i]) {
				max = line[i];
				list = new ArrayList<>();
				list.add(i);
			}
		}
		int answer = 0;
		int left = 0;
		int temp = 0;
		for (int i = 0; i <= list.get(0); i++) {
			if (line[i] < left) {
				temp += left - line[i];
			} else {
				left = line[i];
				answer += temp;
				temp = 0;
			}
		}
		int right = 0;
		temp = 0;
		for (int i = W - 1; i >= list.get(list.size() - 1); i--) {
			if (line[i] < right) {
				temp += right - line[i];
			} else {
				right = line[i];
				answer += temp;
				temp = 0;
			}
		}
		
		for (int i = 0; i < list.size() - 1; i++) {
			for (int j = list.get(i); j < list.get(i + 1); j++) {
				answer += max - line[j];
			}
		}
		
		System.out.println(answer);
	}
	
}
