import java.io.*;
import java.util.*;

class Pair implements Comparable<Pair> {
	int num, cnt;
	Pair (int num, int cnt) {
		this.num = num;
		this.cnt = cnt;
	}
	
	@Override
	public int compareTo(Pair o) {
		int compare = Integer.compare(this.cnt, o.cnt);
		if (compare == 0) {
			return Integer.compare(this.num, o.num);
		}
		return compare;
	}
	
}

public class Main {
	
	static int r, c, k;
	static int[][] A = new int[101][101];
	static int xLen = 3, yLen = 3;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= 3; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 1; j <= 3; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		System.out.println(solution());
	}
	
	static int solution() {
		for (int time = 0; time <= 100; time++) {
			if (A[r][c] == k) {
				return time;
			}
			operating();
		}
		return -1;
	}
	
	static void operating() {
		if (xLen >= yLen) {
			for (int i = 1; i <= xLen; i++) {
				R(i);
			}
		} else {
			for (int i = 1; i <= yLen; i++) {
				C(i);
			}
		}
	}
	static void R(int key) {
		PriorityQueue<Pair> pq = new PriorityQueue<>();
		Map<Integer, Integer> map = new HashMap<>();
		
		for (int i = 1; i <= yLen; i++) {
			if (A[key][i] == 0)	continue;
			map.compute(A[key][i], (num, count) -> count == null ? 1 : count + 1);
		}
		
		map.forEach((k, v) -> pq.add(new Pair(k, v)));
		
		int i = 1;
		while (!pq.isEmpty()) {
			Pair p = pq.poll();
			A[key][i++] = p.num;
			A[key][i++] = p.cnt;
		}
		
		yLen = Math.max(yLen, i);
		
		while (i <= 99) {
			A[key][i++] = 0;
			A[key][i++] = 0;
		}
	}
	
	static void C(int key) {
		PriorityQueue<Pair> pq = new PriorityQueue<>();
		Map<Integer, Integer> map = new HashMap<>();
		
		for (int i = 1; i <= xLen; i++) {
			if (A[i][key] == 0)	continue;
			map.compute(A[i][key], (num, count) -> count == null ? 1 : count + 1);
		}
		
		map.forEach((k, v) -> pq.add(new Pair(k, v)));
		
		int i = 1;
		while (!pq.isEmpty()) {
			Pair p = pq.poll();
			A[i++][key] = p.num;
			A[i++][key] = p.cnt;
		}
		
		xLen = Math.max(xLen, i);
		
		while (i <= 99) {
			A[i++][key] = 0;
			A[i++][key] = 0;
		}
	}
}
