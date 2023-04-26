import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> minQueue = new PriorityQueue<>();
		for (int i = 0; i < n; i++) {
			int x = Integer.parseInt(br.readLine());
			if (x > 0)
				minQueue.add(x);
			else {
				if (!minQueue.isEmpty()) {
					sb.append(minQueue.poll() + "\n");
				} else {
					sb.append(0 + "\n");
				}
			}
		}
		System.out.println(sb);
	}

}
