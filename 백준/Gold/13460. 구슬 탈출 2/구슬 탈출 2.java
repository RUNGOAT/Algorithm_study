import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main
{
	static int N, M;
	static int min = Integer.MAX_VALUE;
	static BufferedWriter bw;
	static boolean blueBallOut = false;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	
    	N = Integer.parseInt(st.nextToken());
    	M = Integer.parseInt(st.nextToken());
    	
    	char[][] map = new char[N][M];
    	for (int i = 0; i < N; i++) {
    		String line = br.readLine();
    		for (int j = 0; j < M; j++) {
    			map[i][j] = line.charAt(j);
    		}
    	}
    	
    	// dfs 로 지속적으로 새로운 맵을 만들어서 확인한다.
    	dfs(map, 1);
    	
    	if (min == Integer.MAX_VALUE) {
    		bw.write(-1 + "\n");
    	} else {
    		bw.write(min + "\n");    		
    	}
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static void dfs(char[][] map, int round) throws IOException {
    	if (round > 10) {
    		blueBallOut = false;
    		return;
    	}
    	if (blueBallOut) {
    		blueBallOut = false;
    		return;
    	}
    	
//    	print(map);
//		System.out.println();
    	
    	// 4가지 기울이기 함수를 생성한다.
    	char[][] newMap = copy(map);
    	if (moveWidth(1, M-2, 1, newMap)) {
    		min = Math.min(min, round);
    		return;
    	} else {
    		dfs(newMap, round+1);
    	}
    	
    	newMap = copy(map);
    	if (moveWidth(M-2, 1, -1, newMap)) {
    		min = Math.min(min, round);
    		return;
    	} else {
    		dfs(newMap, round+1);
    	}
    	
    	newMap = copy(map);
    	if (moveLength(1, N-2, 1, newMap)) {
    		min = Math.min(min, round);
    		return;
    	} else {
    		dfs(newMap, round+1);
    	}
    	
    	newMap = copy(map);
    	if (moveLength(N-2, 1, -1, newMap)) {
    		min = Math.min(min, round);
    		return;
    	} else {
    		dfs(newMap, round+1);
    	}
    }
    
    // 기울이기 함수
    // R 또는 B를 만나면 해당 기울이기 방향으로 이동시킨다.
    // 이 과정에서 R이 O를 만나면 불리언 값 true 바꿔주고
    // 만약 B가 O를 만나게 되면 불가능한 경우로 불리언 값을 false로 다시 바꾸고 return 한다.
    static boolean moveWidth(int start, int end, int value, char[][] map) {
    	boolean redBallOut = false;
    	for (int i = 1; i < N-1; i++) {
    		for (int j = end - value; j != start - (2 * value); j -= value) {
    			if (map[i][j] == 'R') {
    				int k = j + value;
    				while (k != end + (2 * value)) {
    					if (map[i][k] == 'O') {
    						redBallOut = true;
    						map[i][j] = '.';
    						break;
    					} else if (map[i][k] == 'B' || map[i][k] == '#') {
    						map[i][j] = '.';
    						map[i][k - value] = 'R';
    						break;
    					}
    					k += value;
    				}
    			} else if (map[i][j] == 'B') {
    				int k = j + value;
    				while (k != end + (2 * value)) {
    					if (map[i][k] == 'O') {
    						redBallOut = false;
    						blueBallOut = true;
    						return false;
    					} else if (map[i][k] == 'R' || map[i][k] == '#') {
    						map[i][j] = '.';
    						map[i][k - value] = 'B';
    						break;
    					}
    					k += value;
    				}
    			}
    		}
    		if (redBallOut) {
    			blueBallOut = false;
    			return true;
    		}
    	}
    	blueBallOut = false;
    	return false;
    }
    
    static boolean moveLength(int start, int end, int value, char[][] map) {
    	boolean redBallOut = false;
    	for (int j = 1; j < M-1; j++) {
    		for (int i = end - value; i != start - (2 * value); i -= value) {
    			if (map[i][j] == 'R') {
    				int k = i + value;
    				while (k != end + (2 * value)) {
    					if (map[k][j] == 'O') {
    						redBallOut = true;
    						map[i][j] = '.';
    						break;
    					} else if (map[k][j] == 'B' || map[k][j] == '#') {
    						map[i][j] = '.';
    						map[k - value][j] = 'R';
    						break;
    					}
    					k += value;
    				}
    			} else if (map[i][j] == 'B') {
    				int k = i + value;
    				while (k != end + (2 * value)) {
    					if (map[k][j] == 'O') {
    						redBallOut = false;
    						blueBallOut = true;
    						return false;
    					} else if (map[k][j] == 'R' || map[k][j] == '#') {
    						map[i][j] = '.';
    						map[k - value][j] = 'B';
    						break;
    					}
    					k += value;
    				}
    			}
    		}
    		if (redBallOut) {
    			blueBallOut = false;
    			return true;
    		}
    	}
    	blueBallOut = false;
    	return false;
    }
    
    static char[][] copy(char[][] map) {
    	char[][] copy = new char[N][M];
    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < M; j++) {
    			copy[i][j] = map[i][j];
    		}
    	}
    	return copy;
    }
    
    static void print(char[][] map) throws IOException {
    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < M; j++) {
    			bw.write(map[i][j] + " ");
    		}
    		bw.write("\n");
    	}
    }
}