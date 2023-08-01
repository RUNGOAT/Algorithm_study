import java.util.*;
import java.io.*;

class Point {
    int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main
{
    static int H, W;
    static char[][] arr;
    static boolean[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static char[] direction = {'>', 'v', '<', '^'};
    static StringBuilder sb;

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        List<Point> list = new ArrayList<>();   // 로봇이 지나간 경로의 위칫값
        arr = new char[H][W];
        for (int i = 0; i < H; i++) {
            String temp = br.readLine();
            for (int j = 0; j < W; j++) {
                arr[i][j] = temp.charAt(j);
                if (temp.charAt(j) == '#') {
                    list.add(new Point(i, j));
                }
            }
        }

        Point start = new Point(0, 0);    // 로봇의 시작점
        int startDirection = -1; // 처음 로봇이 바라보는 방향
        for (Point point : list) {
            int d = isStartPoint(point);
            if (d != -1) {
                start = point;
                startDirection = d;
                break;
            }
        }

        sb = new StringBuilder();
        sb.append(start.x + 1).append(" ").append(start.y + 1).append("\n");
        sb.append(direction[startDirection]).append("\n");

        dfs(start.x, start.y, startDirection, 0);

        System.out.println(sb.toString());
    }

    static void dfs(int x, int y, int d, int cnt) {

        int nx = x + dx[d];
        int ny = y + dy[d];
        if (cnt == 1) {
            dfs(nx, ny, d, cnt + 1);
            return;
        }
        // 로봇은 방향을 전환할 때 L or R로 한 번 움직인 후 A를 하게 된다.
        if (rangeOut(nx, ny) || arr[nx][ny] == '.') {
            int l = (d + 3) % 4;
            nx = x + dx[l];
            ny = y + dy[l];
            if (!rangeOut(nx, ny) && arr[nx][ny] == '#') {
                sb.append("L");
                d = l;
            } else {
                int r = (d + 1) % 4;
                nx = x + dx[r];
                ny = y + dy[r];
                if (rangeOut(nx, ny) || arr[nx][ny] == '.') {
                    return;
                }
                sb.append("R");
                d = r;
            }
        }
        sb.append("A");
        dfs(nx, ny, d, 1);
    }

    static int isStartPoint(Point point) {
        // 한 바퀴 돌면서 만약 갈 수 없는 곳이면 += 0
        // 2칸 전진할 수 있으면 += 1
        // 만약 값이 2를 넘어가면 false 리턴
        // 값이 1이 나오면 true 리턴

        int count = 0;
        int direction = -1;
        for (int d = 0; d < 4; d++) {
            int nx = point.x + dx[d];
            int ny = point.y + dy[d];
            if (rangeOut(nx, ny)) continue;
            if (arr[nx][ny] == '#') {
                count += 1;
                int nnx = nx + dx[d];
                int nny = ny + dy[d];
                if (rangeOut(nnx, nny)) continue;
                if (arr[nnx][nny] == '#') {
                    direction = d;
                }
            }
        }
        if (count == 1) {
            return direction;
        }
        return -1;
    }

    static boolean rangeOut(int x, int y) {
        return 0 > x || H <= x || 0 > y || W <= y;
    }
}
