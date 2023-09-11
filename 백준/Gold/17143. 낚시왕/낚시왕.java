import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Shark {
    int id, x, y, speed, d, size;

    public Shark(int id, int x, int y, int speed, int d, int size) {
        this.id = id;
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.d = d;
        this.size = size;
    }
}

public class Main {

    static int R, C, M;
    static List<Shark>[][] map;
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
        map = new ArrayList[R+1][C+1];
        for (int i = 1; i <= R; i++) {
        	for (int j = 1; j <= C; j++) {
        		map[i][j] = new ArrayList<>();
        	}
        }
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int speed = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int size = Integer.parseInt(st.nextToken());
            
            sharks[i] = new Shark(i, x, y, speed, d, size);
            map[x][y].add(new Shark(i, x, y, speed, d, size));
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
        for (int i = 0; i < M; i++) {
            Shark shark = sharks[i];
            
            if (shark == null)    continue;
            
            int cnt = 0;
            int end = getEndPoint(shark, shark.d);
            
            while (cnt < end) {
	            int d = shark.d;
	            int nx = shark.x + dx[d];
	            int ny = shark.y + dy[d];
	            if (rangeOut(nx, ny)) {
	                d = changeDirection(d);
	                nx = shark.x + dx[d];
	                ny = shark.y + dy[d];
	                shark.d = d;
	            }
	            cnt++;
	            shark.x = nx;
	            shark.y = ny;
            }
        }
        
        for (int i = 1; i <= R; i++) {
        	for (int j = 1; j <= C; j++) {
        		map[i][j] = new ArrayList<>();
        	}
        }
        
        for (int i = 0; i < M; i++) {
            Shark shark = sharks[i];
            if (shark == null)	continue;
            map[shark.x][shark.y].add(shark);
        }
        
        for (int i = 1; i <= R; i++) {
        	for (int j = 1; j <= C; j++) {
        		if (map[i][j].size() <= 1)	continue;
				Shark shark = max(map[i][j]);
				map[i][j] = new ArrayList<>();
				map[i][j].add(shark);
        	}
        }
    }
    
    static Shark max(List<Shark> list) {
    	Shark res = new Shark(-1, -1, -1, -1, -1, -1);
    	for (Shark shark : list) {
    		if (shark.size > res.size) {
    			res = shark;
    		}
    	}
    	for (Shark shark : list) {
    		if (shark.id != res.id) {
    			sharks[shark.id] = null;
    		}
    	}
    	return res;
    }
    
    static int catchShark(int c) {
        for (int r = 1; r <= R; r++) {
            if (!map[r][c].isEmpty()) {
                Shark shark = map[r][c].get(0);
                int size = shark.size;
                sharks[shark.id] = null;
                map[r][c] = new ArrayList<>();
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
