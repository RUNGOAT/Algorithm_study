import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main
{
	static int N, L;
	static int[][] map;
	static int answer = 0;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	N = Integer.parseInt(st.nextToken());
    	L = Integer.parseInt(st.nextToken());
    	map = new int[N][N];
    	for (int i = 0; i < N; i++) {
    		st = new StringTokenizer(br.readLine(), " ");
    		for (int j = 0; j < N; j++) {
    			map[i][j] = Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	for (int i = 0; i < N; i++) {
    		if (checkRow(i))	answer++;
    		if (checkColumn(i))	answer++;
    	}
    	
    	bw.write(answer + "\n");
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static boolean checkRow (int row) {
    	boolean[] incline = new boolean[N];
    	
    	for (int i = 0; i < N-1; i++) {
    		int diff = map[row][i] - map[row][i+1];
    		
    		if (diff > 1 || diff < -1)	return false;
    		else if(diff == 1) {
    			for (int j = 1; j <= L; j++) {
    				if (i + j >= N || incline[i + j])
    					return false;
    				if (map[row][i] - 1 != map[row][i+j])
    					return false;
    				incline[i + j] = true;
    			}
    		}
    		else if (diff == -1) {
    			for (int j = 0; j < L; j++) {
    				if (i - j < 0 || incline[i - j])
    					return false;
    				if (map[row][i] != map[row][i - j])
    					return false;
    				incline[i - j] = true;
    			}
    		}
    	}
    	return true;
    }
    
    static boolean checkColumn (int column) {
    	boolean[] incline = new boolean[N];
    	
    	for (int i = 0; i < N-1; i++) {
    		int diff = map[i][column] - map[i+1][column];
    		
    		if (diff > 1 || diff < -1)	return false;
    		else if(diff == 1) {
    			for (int j = 1; j <= L; j++) {
    				if (i + j >= N || incline[i + j])
    					return false;
    				if (map[i][column] - 1 != map[i+j][column])
    					return false;
    				incline[i + j] = true;
    			}
    		}
    		else if (diff == -1) {
    			for (int j = 0; j < L; j++) {
    				if (i - j < 0 || incline[i - j])
    					return false;
    				if (map[i][column] != map[i - j][column])
    					return false;
    				incline[i - j] = true;
    			}
    		}
    	}
    	return true;
    }
}
