import java.util.*;
import java.io.*;

public class Main {
	
    static int N;
    static int[][] arr;
    static int[] pointers;
    static int answer;
    static int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int M = 3 * N;
        arr = new int[M][N];
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                arr[M-1-i][j] = Integer.parseInt(st.nextToken());
            }
        }

        pointers = new int[N];			// 위에서 떨어질 차량을 가리키는 위칫값
        int[][] box = new int[N][N];	// 차고
        answer = 0;

        simulation(box, 0, 1, 0, 0, N - 1);

        System.out.println(answer);
    }

    /**
     * @param box 차고
     * @param score 회차의 점수
     * @param round 회차
     * @param b bottom
     * @param l left
     * @param r right
     */
    static void simulation(int[][] box, int score, int round, int b, int l, int r) {
    	if (answer < score) {
    		answer = score;
    	}

        if (round == 4)
            return;

        initBox(box, b, l, r);
        int[][] nowBox = new int[N][N];
        for (int i = 0; i < N; i++) {
            nowBox[i] = Arrays.copyOf(box[i], N);
        }
        int[] savedPointers = Arrays.copyOf(pointers, N);

        boolean[][] visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j])
                    continue;
                int[] res = bfs(i, j, visited, nowBox);
                int plus = res[0];
                b = res[1];
                l = res[2];
                r = res[3];
                simulation(nowBox, score + plus, round + 1, b, l, r);
                copyPointers(savedPointers, l, r);
                copyBox(nowBox, box, b, l, r);
            }
        }
    }
  
    /**
     * 
     * @param sx
     * @param sy
     * @param visited
     * @param box
     * @return box[sx][sy]를 선택했을 때 얻을 수 있는 점수,
            사라진 자동차들을 포함하는 가장 작은 직사각형 범위 b, l, r
     */
    static int[] bfs(int sx, int sy, boolean[][] visited, int[][] box) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{sx, sy});
        visited[sx][sy] = true;
        int color = box[sx][sy];
        int cnt = 1;

        int minX = 16, minY = 16, maxX = 0, maxY = 0;
        while (!stack.isEmpty()) {
            int[] pos = stack.pop();
            int x = pos[0], y = pos[1];
            box[x][y] = 0;
            minX = Math.min(minX, x);
            maxX = Math.max(maxX, x);
            minY = Math.min(minY, y);
            maxY = Math.max(maxY, y);
            for (int[] dir : directions) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx < 0 || nx >= N || ny < 0 || ny >= N || color != box[nx][ny] || visited[nx][ny])
                    continue;
                stack.push(new int[]{nx, ny});
                visited[nx][ny] = true;
                cnt++;
            }
        }

        return new int[] {cnt + (maxX - minX + 1) * (maxY - minY + 1), minX, minY, maxY};
    }
  
    /**
     * 차고에 빈 자리가 있으면 아래로 채운 뒤 남은 자리는 위에서 떨어지는 자동차로 채운다.
     * 
     * @param box 차고
     * @param b bottom
     * @param l left
     * @param r right
     */
    static void initBox(int[][] box, int b, int l, int r) {
        for (int j = l; j <= r; j++) {
            int pointer = pointers[j];
            for (int si = b; si < N; si++) {
                int i = si;
                if (box[i][j] == 0) {
                    boolean flag = true;
                    while (i < N) {	// 빈 자리가 있으면 아래로 채우기
                        if (box[i][j] != 0) {
                            box[si][j] = box[i][j];
                            box[i][j] = 0;
                            flag = false;
                            break;
                        }
                        i++;
                    }
                    if (flag) {	// 위에서 떨어지는 자동차로 채우기
                        box[si][j] = arr[pointer][j];
                        pointer++;
                    }
                }
            }
            pointers[j] = pointer;
        }
    }
    
    static void copyPointers(int[] savedPointers, int l, int r) {
        for (int i = l; i <= r; i++) {
            pointers[i] = savedPointers[i];
        }
    }
  
    static void copyBox(int[][] nowBox, int[][] box, int b, int l, int r) {
        for (int j = l; j <= r; j++) {
            for (int i = b; i < N; i++) {
                nowBox[i][j] = box[i][j];
            }
        }
    }
}
