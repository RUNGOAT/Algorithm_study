import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main
{
	static int N;
	static short[] arr;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	N = Integer.parseInt(br.readLine());
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	
    	arr = new short[N];
    	for (int i = 0; i < N; i++) {
    		arr[i] = Short.parseShort(st.nextToken());
    	}
    	
    	int answer = 0;
    	
    	// 벌통 오른 끝
    	int first = sum(1, N);
    	answer = Math.max(answer, findMaxHoney(1, N-1, 1, first));
    	
    	// 벌통 왼 끝
    	first += arr[0] - arr[N-1];
    	answer = Math.max(answer, findMaxHoney(N-2, 0, -1, first));
    	
    	// 벌통 중간쯤
    	// 벌통 = i
    	// 벌통은 벌 두 마리가 방문한다.
    	int ggul = first - arr[0];
    	for (int i = 1; i < N-1; i++) {
    		answer = Math.max(answer, ggul + arr[i]);
    	}
    	
    	bw.write(answer + "\n");
    	bw.flush();
    	bw.close();
    	br.close();
	}
    
    static int findMaxHoney(int start, int end, int value, int first) {
    	int answer = 0;
    	
    	int second = first;	// 반복문에서 시작값을 뺄 예정
    	for (int i = start; i != end; i += value) {
    		int secondStart = arr[i];
    		second -= secondStart;
    		answer = Math.max(answer, first + second - secondStart);
    	}
    	
    	return answer;
    }
    
    static int sum(int start, int end) {
    	int sum = 0;
    	for (int i = start; i < end; i++) {
    		sum += arr[i];
    	}
    	return sum;
    }
}