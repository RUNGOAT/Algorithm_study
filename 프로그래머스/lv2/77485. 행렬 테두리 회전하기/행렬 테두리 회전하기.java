class Solution {
    
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] arr = new int[rows][columns];
        
        int number = 1;
        for (int i = 0; i < rows; i++) {
        	for (int j = 0; j < columns; j++) {
        		arr[i][j] = number++;
        	}
        }
        
        int idx = 0;
        for (int[] query : queries) {
            int x1 = query[0] - 1;
            int y1 = query[1] - 1;
            int x2 = query[2] - 1;
            int y2 = query[3] - 1;
            
            int before = arr[x1][y1];
            int d = 0;
            int x = x1;
            int y = y1;
            int min = Integer.MAX_VALUE;
           while (true)  {
               min = Math.min(min, before);
               int nx = x + dx[d];
               int ny = y + dy[d];
               
               if (x1 > nx || x2 < nx || y1 > ny || y2 < ny) {
                   d++;
                   if (d == 4) {
                       break;
                   }
                   nx = x + dx[d];
                   ny = y + dy[d];
               }
               
               int tmp = arr[nx][ny];
               arr[nx][ny] = before;
               before = tmp;
               
               x = nx;
               y = ny;
           }
            answer[idx++] = min;
        }
        
        return answer;
    }
}