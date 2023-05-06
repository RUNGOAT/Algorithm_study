import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Truck {
	int weight, time;

	public Truck(int weight, int time) {
		super();
		this.weight = weight;
		this.time = time;
	}

}

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int n = Integer.parseInt(st.nextToken());
		int w = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());

		int[] trucks = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			trucks[i] = Integer.parseInt(st.nextToken());
		}

		Queue<Truck> q = new LinkedList<>();
		int time = 0;
		int crossed = 0;
		int idx = 0;
		int sum = 0;
		while (crossed < n) {
			time++;
			if (!q.isEmpty() && time - q.peek().time == w) {
				sum -= q.remove().weight;
				crossed++;
			}

			if (idx < n && sum + trucks[idx] <= L) {
				q.add(new Truck(trucks[idx], time));
				sum += trucks[idx];
				idx++;
			}

		}
		System.out.println(time);
	}

}
