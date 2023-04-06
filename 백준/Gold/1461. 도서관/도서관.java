import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static int N, M;
	static int[] line;
	static List<Integer> negative;
	static List<Integer> positive;
	static int answer;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		positive = new ArrayList<>();
		negative= new ArrayList<>();
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			if (num > 0) {
				positive.add(num);
			}
			else {
				negative.add(num);
			}
		}
		
		Collections.sort(negative);
		Collections.sort(positive, Collections.reverseOrder());
		
		answer = 0;
		if (positive.size() == 0) {
			answer += Math.abs(negative.get(0));
			check(negative, M);
		}
		else if (negative.size() == 0) {
			answer += positive.get(0);
			check(positive, M);
		}
		else if (positive.get(0) > Math.abs(negative.get(0))) {
			answer += positive.get(0);
			check(positive, M);
			check(negative, 0);
		}
		else {			
			answer += Math.abs(negative.get(0));
			check(negative, M);
			check(positive, 0);
		}
		
		System.out.println(answer);
		
	}
	
	static void check(List<Integer> list, int start) {
		for (int i = start; i < list.size(); i += M) {
			answer += Math.abs(list.get(i)) * 2;
		}
	}
	
}
