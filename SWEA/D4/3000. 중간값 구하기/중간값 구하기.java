import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
	

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			bw.write("#" + t + " ");
			int answer = 0;
			
			st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int mid = Integer.parseInt(st.nextToken());
			
			PriorityQueue<Integer> left = new PriorityQueue<>(new Comparator<Integer>() {
				@Override
				public int compare(Integer o1, Integer o2) {
					return Integer.compare(o2, o1);
				}
			});
			
			PriorityQueue<Integer> right = new PriorityQueue<>(new Comparator<Integer>() {
				@Override
				public int compare(Integer o1, Integer o2) {
					return Integer.compare(o1, o2);
				}
			});
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				if (mid > x)	left.offer(x);
				else			right.offer(x);
				
				if (mid > y)	left.offer(y);
				else			right.offer(y);
				
				int leftSize = left.size();
				int rightSize = right.size();
				
				if (leftSize > rightSize) {
					right.offer(mid);
					mid = left.poll();
				}
				else if (leftSize < rightSize) {
					left.offer(mid);
					mid = right.poll();
				}
				
				answer = (answer + mid) % 20171109;
			}
			
			bw.write(answer + "\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}
}
