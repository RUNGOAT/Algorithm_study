import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Point implements Comparable<Point> {
	int x, y;
	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	@Override
	public int compareTo(Point o) {
		if (this.y == o.y) {
			return Integer.compare(this.x, o.x);			
		}
		return Integer.compare(this.y, o.y);
	}
}

public class Main {

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		Point[] arr = new Point[N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			arr[i] = new Point(x, y);
		}
		
		Arrays.sort(arr);
		
		for (int i = 0; i < N; i++) {
			bw.write(arr[i].x + " " + arr[i].y + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
	
}