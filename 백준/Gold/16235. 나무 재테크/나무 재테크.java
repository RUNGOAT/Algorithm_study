import java.io.*;
import java.util.*;

public class Main {
	
	static int N, M, K;
	static int[][] A;
	static int[][] map;
	static List<Integer>[][] trees;
	static int[][] diedTree;
	static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
	static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = 5;
			}
		}
		
		A = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		trees = new ArrayList[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				trees[i][j] = new ArrayList<Integer>();
			}
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken()) - 1;
			int y = Integer.parseInt(st.nextToken()) - 1;
			int z = Integer.parseInt(st.nextToken());
			
			trees[x][y].add(z);
		}
		
		diedTree = new int[N][N];
		
		for (int k = 0; k < K; k++) {
			spendFirstHalf();
			spendSecondHalf();
		}
		
		int count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				count += trees[i][j].size();
			}
		}
		System.out.println(count);
	}
	
	// 봄 - 자신의 나이만큼 양분을 먹음(한 칸에 여러 개면 어린 나무부터, 나이만큼 양분을 못 먹으면 죽음) -> 나이가 1 증가
	static void spendFirstHalf() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				List<Integer> treeList = trees[i][j];
				Collections.sort(treeList);
				List<Integer> newTree = new ArrayList<>();
				for (int age : treeList) {
					if (age <= map[i][j]) {
						map[i][j] -= age;
						newTree.add(++age);
					} else {
						// 여름 - 봄에 죽은 나무가 양분으로 변함 (나이를 2로 나눈 값이 해당 칸에 추가됨)
						diedTree[i][j] += age / 2;
					}
				}
				map[i][j] += diedTree[i][j];
				diedTree[i][j] = 0;
				trees[i][j] = newTree;
			}
		}
	}
	
	// 가을 - 번식 (나이가 5의 배수인 나무, 인접한 8개의 칸, map 벗어나면 안됨)
	static void spendSecondHalf() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				for (int age : trees[i][j]) {
					if (age % 5 == 0) {
						for (int d = 0; d < 8; d++) {
							int nx = i + dx[d];
							int ny = j + dy[d];
							if (0 > nx || N <= nx || 0 > ny || N <= ny)
								continue;
							trees[nx][ny].add(1);
						}
					}
				}
				// 겨울 - 양분을 추가 A[r][c]의 값이 추가됨
				map[i][j] += A[i][j];
			}
		}
	}
}
