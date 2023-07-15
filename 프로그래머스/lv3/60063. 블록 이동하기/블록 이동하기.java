import java.util.*;

class Solution {
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};
    private static final int[][][] rotation = {
        {{-1, 0, -1, 0}, {0, 0, 1, 1}},
        {{0, 0, 1, 1}, {-1, 0, -1, 0}}
    };

    private class Robot {
        int x, y, dir, count;
        Robot(int x, int y, int dir, int count) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.count = count;
        }
    }

    public int solution(int[][] board) {
        int len = board.length;
        int answer = Integer.MAX_VALUE;
        boolean[][][] visited = new boolean[2][len][len];
        Queue<Robot> queue = new LinkedList<>();

        queue.add(new Robot(0, 0, 0, 0));
        visited[0][0][0] = true;

        while(!queue.isEmpty()) {
            Robot cur = queue.poll();

            if((cur.dir == 0 && cur.x == len - 1 && cur.y == len - 2) || 
               (cur.dir == 1 && cur.x == len - 2 && cur.y == len - 1)) {
                answer = Math.min(answer, cur.count);
                continue;
            }

            // 상하좌우 이동
            for(int i = 0; i < 4; i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if(canMove(nx, ny, cur.dir, board) && !visited[cur.dir][nx][ny]) {
                    queue.add(new Robot(nx, ny, cur.dir, cur.count + 1));
                    visited[cur.dir][nx][ny] = true;
                }
            }

            // 회전
            for(int i = 0; i < 4; i++) {
                int nx = cur.x + rotation[cur.dir][0][i];
                int ny = cur.y + rotation[cur.dir][1][i];
                
                // 가로 방향
                int cx = cur.x + dx[i%2];
                int cy = cur.y + dy[i%2];
                
                if (cur.dir == 1) {
                	cx = cur.x + dx[i < 2 ? i + 2 : i];
                	cy = cur.y + dy[i < 2 ? i + 2 : i];
                }
                int ndir = cur.dir ^ 1;
                
                if (!canMove(nx, ny, ndir, board) || !canMove(cx, cy, cur.dir, board))
                	continue;
                if(!visited[ndir][nx][ny]) {
                    queue.add(new Robot(nx, ny, ndir, cur.count + 1));
                    visited[ndir][nx][ny] = true;
                }
            }
        }
        return answer;
    }

    private boolean canMove(int nx, int ny, int dir, int[][] board){
        int len = board.length;
        if(dir == 0){
            return !(nx < 0 || ny < 0 || nx >= len || ny + 1 >= len 
            		|| board[nx][ny] != 0 || board[nx][ny + 1] != 0);
        } else {
            return !(nx < 0 || ny < 0 || nx + 1 >= len || ny >= len 
            		|| board[nx][ny] != 0 || board[nx + 1][ny] != 0);
        }
    }
}
