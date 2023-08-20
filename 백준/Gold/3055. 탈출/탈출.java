import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
	int r, c;
    int time;

	public Node(int r, int c, int time) {
		this.r = r;
		this.c = c;
		this.time = time;
	}
}

public class Main
{

	static int R, C;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};

    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    	R = Integer.parseInt(st.nextToken());
    	C = Integer.parseInt(st.nextToken());
        
        Queue<Node> wq = new LinkedList<>();        
        Queue<Node> sq = new LinkedList<>();

    	char[][] arr = new char[R][C];

    	for (int i = 0; i < R; i++) {
    		String line = br.readLine();
    		for (int j = 0; j < C; j++) {
    			arr[i][j] = line.charAt(j);
    			if (arr[i][j] == '*') {
                    wq.add(new Node(i, j, 0));
    			} else if (arr[i][j] == 'S') {
                    sq.add(new Node(i, j, 0));
    			}
    		}
    	}

    	int answer = solution(arr, wq, sq);
    	if (answer == -1) {
    		bw.write("KAKTUS\n");
    	} else {
    		bw.write(answer + "\n");
    	}    	

    	bw.flush();
    	bw.close();
    	br.close();
    }  

    static int solution(char[][] arr, Queue<Node> wq, Queue<Node> sq) {  	

    	while (!sq.isEmpty()) {
    		int wSize = wq.size();
    		for (int i = 0; i < wSize; i++) {
    			Node wNode = wq.poll();
    			for (int d = 0; d < 4; d++) {
    				int nx = wNode.r + dx[d];
    				int ny = wNode.c + dy[d];
    				if (rangeOut(nx, ny))	continue;
    				if (arr[nx][ny] != '.')	continue;
    				arr[nx][ny] = '*';
    				wq.add(new Node(nx, ny, 0));
    			}
    		}

    		int sSize = sq.size();
    		for (int i = 0; i < sSize; i++) {
    			Node sNode = sq.poll();

    			for (int d = 0; d < 4; d++) {
    				int nx = sNode.r + dx[d];
    				int ny = sNode.c + dy[d];
    				if (rangeOut(nx, ny))	continue;
    				if (arr[nx][ny] == 'D') {
    					return sNode.time + 1;
    				}
    				if (arr[nx][ny] != '.')	continue;
    				arr[nx][ny] = 'S';
    				sq.add(new Node(nx, ny, sNode.time + 1));
    			}
    		}
    	}
    	return -1;
    }

    static boolean rangeOut(int x, int y) {
    	return 0 > x || R <= x || 0 > y || C <= y;
    }
}