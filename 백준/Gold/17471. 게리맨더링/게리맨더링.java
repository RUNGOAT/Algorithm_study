import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Position {
	int area, peopleNum;
	
	Position(int area, int peopleNum) {
		this.area = area;
		this.peopleNum = peopleNum;
	}
}

public class Main {
	
	static int N;
	static Position[] positions;
	static ArrayList<Integer>[] graph;
	static int answer = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		N = Integer.parseInt(br.readLine());
		
		positions = new Position[N+1];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 1; i <= N; i++) {
			int peopleNum = Integer.parseInt(st.nextToken());
			positions[i] = new Position(i, peopleNum);
		}
		
		graph = new ArrayList[N+1];
		for (int i = 0; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(st.nextToken());
			for (int j = 0; j < n; j++) {
				int area = Integer.parseInt(st.nextToken());
				graph[i].add(area);
			}
		}
		
		ArrayList<Integer> A = new ArrayList<>();
		for (int i = 1; i <= N / 2; i++) {
			comb(1, N, i, A);	// 조합으로 지역 분리
		}
		
		if (answer == Integer.MAX_VALUE) {
			answer = -1;
		}
		
		bw.write(answer + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
	
	static void comb(int start, int n, int r, ArrayList<Integer> A) {
		if (r == 0) {
			gerrymandering(A);
			return;
		}
		
		for (int i = start; i <= n; i++) {
			A.add(i);
			comb(i + 1, n, r - 1, A);
			A.remove(A.size() - 1);
		}
	}
	
	// 할당받은 지역의 인구 수의 차이 계산
	static void gerrymandering(ArrayList<Integer> A) {
		// A 지역 선거구 연결 확인
		if (!isConnect(positions[A.get(0)].area, A)) {
			return;
		}
		
		ArrayList<Integer> B = new ArrayList<>();
		for (int i = 1; i <= N; i++) {
			if (A.contains(i)) {
				continue;
			}
			B.add(i);
		}
		
		// B 지역 선거구 연결 확인
		if (!isConnect(positions[B.get(0)].area, B)) {
			return;
		}
		
		int resultA = 0;	// A 지역 인구 총합
		for (int i = 0; i < A.size(); i++) {
			resultA += positions[A.get(i)].peopleNum;
		}
		
		int resultB = 0;	// B 지역 인구 총합
		for (int i = 0; i < B.size(); i++) {
			resultB += positions[B.get(i)].peopleNum;
		}
		
		int result = Math.abs(resultA - resultB);
		answer = Math.min(answer, result);
	}
	
	// 선거구 연결 확인
	static boolean isConnect(int num, ArrayList<Integer> arr) {
		boolean[] visited = new boolean[N+1];
		visited[num] = true;
		Queue<Integer> q = new LinkedList<>();
		q.offer(num);
		
		int count = 1;
		while (!q.isEmpty()) {
			int start = q.poll();
			
			for (int i : graph[start]) {
				if (visited[i])	continue;
				if (!arr.contains(i))	continue;
				visited[i] = true;
				count++;
				q.offer(i);
			}
		}
		
		if (count == arr.size()) {
			return true;
		}
		return false;
	}

}
