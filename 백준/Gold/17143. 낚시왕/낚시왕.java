import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

class Shark {
    int x, y, speed, d, size;

    public Shark(int x, int y, int speed, int d, int size) {
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.d = d;
        this.size = size;
    }
}

public class Main {

    static int R, C, M;
    static Shark[][] map;
    static Shark[] sharks;
    static int answer = 0;
    
    static int[] dx = {0, -1, 1, 0, 0};
    static int[] dy = {0, 0, 0, 1, -1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        sharks = new Shark[M];
        map = new Shark[R+1][C+1];
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int speed = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int size = Integer.parseInt(st.nextToken());
            
            map[x][y] = new Shark(x, y, speed, d, size);
        }

        // 낚시왕 이동
        for (int c = 1; c <= C; c++) {
            // 상어 잡기
            answer += catchShark(c);
            
            // 상어 이동
            moveShark();
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
    
    static void moveShark() {
    	Queue<Shark> q = new LinkedList<>();
    	for (int i = 1; i <= R; i++) {
    		for (int j = 1; j <= C; j++) {
    			if (map[i][j] != null) {
    				// 현재 map에 있는 상어들 Queue에 추가
    				q.offer(new Shark(i, j, map[i][j].speed, map[i][j].d, map[i][j].size));
    			}
    		}
    	}
    	
    	map = new Shark[R+1][C+1];	// 새로운 낚시판
    	
    	// 모든 상어 이동
    	while (!q.isEmpty()) {
    		Shark shark = q.poll();
    		
    		// 상어의 최소 이동 포인트
            int end = getEndPoint(shark, shark.d);
            // 이동
            for (int cnt = 0; cnt < end; cnt++) {
	            int d = shark.d;
	            int nx = shark.x + dx[d];
	            int ny = shark.y + dy[d];
	            if (rangeOut(nx, ny)) {
	                d = changeDirection(d);
	                nx = shark.x + dx[d];
	                ny = shark.y + dy[d];
	                shark.d = d;
	            }
	            shark.x = nx;
	            shark.y = ny;
            }
            
            // 빈 공간인지 확인
            if (map[shark.x][shark.y] != null) {
            	if (map[shark.x][shark.y].size < shark.size) {
            		map[shark.x][shark.y] = new Shark(shark.x, shark.y, shark.speed, shark.d, shark.size);
            	}
            } else {
            	map[shark.x][shark.y] = new Shark(shark.x, shark.y, shark.speed, shark.d, shark.size);
            }
    	}
    }
    
    static int catchShark(int c) {
        for (int r = 1; r <= R; r++) {
            if (map[r][c] != null) {
                Shark shark = map[r][c];
                int size = shark.size;
                map[r][c] = null;
                return size;
            }
        }
        return 0;
    }
    
    static int getEndPoint(Shark shark, int d) {
        int end = 0;
        if (d < 3) {
            end = shark.speed % ((R * 2) - 2);
        } else {
            end = shark.speed % ((C * 2) - 2);
        }
        return end;
    }
    
    static int changeDirection(int d) {
        switch (d) {
            case 1:
                return 2;
            case 2:
                return 1;
            case 3:
                return 4;
            case 4:
                return 3;
        }
        return -1;
    }
    
    static boolean rangeOut(int x, int y) {
        return 1 > x || x > R || 1 > y || y > C;
    }
}
