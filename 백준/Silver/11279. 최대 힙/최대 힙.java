import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder());
		for (int i = 0; i < n; i++) {
			int x = Integer.parseInt(br.readLine());
			if (x > 0)
				maxQueue.add(x);
			else {
				if (!maxQueue.isEmpty()) {
					sb.append(maxQueue.poll() + "\n");
				} else {
					sb.append(0 + "\n");
				}
			}
		}
		System.out.println(sb);
	}

}
