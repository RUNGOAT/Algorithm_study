import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Dice {
    int[][] dice = new int[4][3];
    int[] dx = {0, 0, 0, 1, -1};
    int[] dy = {0, 1, -1, 0, 0};

    void move(int d, int[][] graph, int x, int y) {
        switch (d) {
            case 1: // 동쪽
                int right = dice[1][2];
                int bottom = dice[3][1];
                dice[1][2] = dice[1][1];
                dice[1][1] = dice[1][0];
                dice[1][0] = bottom;
                dice[3][1] = right;
                break;
            case 2: // 서쪽
                int left = dice[1][0];
                bottom = dice[3][1];
                dice[1][0] = dice[1][1];
                dice[1][1] = dice[1][2];
                dice[1][2] = bottom;
                dice[3][1] = left;
                break;
            case 3: // 북쪽
                int temp = dice[0][1];
                for (int i = 0; i < 3; i++) {
                    dice[i][1] = dice[i + 1][1];
                }
                dice[3][1] = temp;
                break;
            case 4: // 남쪽
                temp = dice[3][1];
                for (int i = 3; i > 0; i--) {
                    dice[i][1] = dice[i - 1][1];
                }
                dice[0][1] = temp;
                break;
        }
        if (graph[x][y] == 0) {
            graph[x][y] = dice[3][1];
        } else {
            int temp = graph[x][y];
            graph[x][y] = 0;
            dice[3][1] = temp;
        }
    }

    int getTopFace() {
        return dice[1][1];
    }
}

public class Main {
    static int N, M, K;
    static Dice dice = new Dice();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int x = N - 1 - Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++) {
                graph[N - 1 - i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dice.dice[3][1] = graph[x][y];
        graph[x][y] = 0;

        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < K; i++) {
            int d = Integer.parseInt(st.nextToken());
            int nx = x + dice.dx[d], ny = y + dice.dy[d];
            if (0 > nx || N <= nx || 0 > ny || M <= ny) continue;
            x = nx;
            y = ny;
            dice.move(d, graph, nx, ny);
            sb.append(dice.getTopFace()).append("\n");
        }
        System.out.println(sb.toString());
    }
}
