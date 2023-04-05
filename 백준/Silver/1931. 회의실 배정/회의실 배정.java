import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Time implements Comparable<Time>{
	int start, end;

	public Time(String[] arr) {
		super();
		this.start = Integer.parseInt(arr[0]);
		this.end = Integer.parseInt(arr[1]);
	}

	@Override
	public int compareTo(Time o) {
		if (this.end > o.end) {
			return 1;
		} else if (this.end < o.end) {
			return -1;
		}
		return this.start - o.start;
	}
	
}

public class Main {

	static int N;
	static Time[] times;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		times = new Time[N];
		for (int i = 0; i < N; i++) {
			times[i] = new Time(br.readLine().split(" "));
		}
		
		Arrays.sort(times);
		int answer = 1;
		
		int end = times[0].end;
		for (int i = 1; i < N; i++) {
			if (times[i].start >= end) {
				answer++;
				end = times[i].end;
			}
		}
		
		System.out.println(answer);
		
	}	
}
