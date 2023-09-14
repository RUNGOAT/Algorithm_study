import java.io.*;
import java.util.*;

class Step {
    int rx, ry, bx, by, cnt;

    public Step(int rx, int ry, int bx, int by, int cnt) {
        super();
        this.rx = rx;
        this.ry = ry;
        this.bx = bx;
        this.by = by;
        this.cnt = cnt;
    }
    
}

public class Main {

    static int N, M;
    static char[][] map;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new char[N][M];
        
        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
        }
        
        Step step = new Step(0, 0, 0, 0, 0);
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 'R') {
                	step.rx = i;
                	step.ry = j;
                    map[i][j] = '.';
                } else if (map[i][j] == 'B') {
                	step.bx = i;
                	step.by = j;
                    map[i][j] = '.';
                }
            }
        }
        
        bw.write(bfs(step) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
    
    static int bfs(Step cur) {
        Queue<Step> q = new LinkedList<>();
        q.offer(cur);
        
        while (!q.isEmpty()) {
            Step step = q.poll();
            
            // 10번 움직인 경우
            if (step.cnt == 10)        continue;
            
            for (int d = 0; d < 4; d++) {
                int rx = step.rx;
                int ry = step.ry;
                int bx = step.bx;
                int by = step.by;
                boolean isRedHole = false;
                boolean isBlueHole = false;
                
                // 빨간 구슬을 해당 방향으로 벽과 마주할 때까지 이동
                while (true) {
                    int nrx = rx + dx[d];
                    int nry = ry + dy[d];
                    if (map[nrx][nry] == '#')     break;
                    if (map[nrx][nry] == 'O') {
                        isRedHole = true;
                        break;
                    }
                    rx = nrx;
                    ry = nry;
                }
                
                // 파란 구슬을 해당 방향으로 벽과 마주할 때까지 이동
                while (true) {
                	int nbx = bx + dx[d];
                	int nby = by + dy[d];
                	if (map[nbx][nby] == '#')	break;
                	if (map[nbx][nby] == 'O') {
                		// 파란 구슬이 구멍에 빠진 경우
                		isBlueHole = true;
                		break;
                	}
                	bx = nbx;
                	by = nby;
                }
                
                // 만약 파란 구슬이 구멍에 빠졌다면 실패
                if (isBlueHole) {
                	continue;
                } else if (isRedHole) {
                	return step.cnt + 1;
                }
                
                // 두 구슬의 위치가 그대로면 큐에 삽입하지 않고 패스
                if (step.rx == rx && step.ry == ry & step.bx == bx && step.by == by) {
                	continue;
                }
                
                // 구슬이 같은 선상에 위치해 겹쳐지는 경우에는 구슬이 겹치지 않도록 이동
                if (rx == bx && ry == by) {
                	switch (d) {
                	case 0:
                		if (step.rx < step.bx)	rx--;
                		else	bx--;
                		break;
                	case 1:
                		if (step.rx < step.bx)	bx++;
                		else	rx++;
                		break;
                	case 2:
                		if (step.ry < step.by)	ry--;
                		else	by--;
                		break;
                	case 3:
                		if (step.ry < step.by)	by++;
                		else	ry++;
                	}
                }
                q.offer(new Step(rx, ry, bx, by, step.cnt + 1));
            }
        }
        return -1;
    }
        
}
