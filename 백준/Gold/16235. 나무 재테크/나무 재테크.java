import java.io.*;
import java.util.*;

class Tree implements Comparable<Tree> {
	int x, y, age;
	Tree (int x, int y, int age) {
		this.x = x;
		this.y = y;
		this.age = age;
	}
	
	@Override
	public int compareTo(Tree o) {
		return Integer.compare(this.age, o.age);
	}
	
}

public class Main {
	
	static int N, M, K;
	static int[][] A;
	static int[][] map;
	static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
	static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
	static Deque<Tree> treeList;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		map = new int[N][N];
		A = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
				map[i][j] = 5;
			}
		}
		
		treeList = new LinkedList<>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken()) - 1;
			int y = Integer.parseInt(st.nextToken()) - 1;
			int z = Integer.parseInt(st.nextToken());
			
			treeList.add(new Tree(x, y, z));
		}
		
		for (int k = 0; k < K; k++) {
			spend();
		}
		
		System.out.println(treeList.size());
	}
	
	static void spend() {
		Queue<Tree> diedTree = new LinkedList<>();
		
		// 봄
		for (int i = 0; i < treeList.size();) {
			Tree cur = treeList.pollFirst();
			if (map[cur.x][cur.y] >= cur.age) {
				map[cur.x][cur.y] -= cur.age;
				cur.age++;
				i++;
				treeList.addLast(cur);
			} else {
				diedTree.add(cur);
			}
		}
		
		// 여름
		for (Tree tree : diedTree) {
			map[tree.x][tree.y] += tree.age / 2;
		}
		
		// 가을
		Queue<Tree> possibleList = new LinkedList<>();
		for (Tree tree : treeList) {
			if (tree.age % 5 == 0) {
				possibleList.add(tree);
			}
		}
		while (!possibleList.isEmpty()) {
			Tree tree = possibleList.poll();
			
			for (int d = 0; d < 8; d++) {
				int nx = tree.x + dx[d];
				int ny = tree.y + dy[d];
				if (0 > nx || N <= nx || 0 > ny || N <= ny)
					continue;
				treeList.addFirst(new Tree(nx, ny, 1));
			}
		}
		
		// 겨울
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] += A[i][j];
			}
		}
	}
	
}
