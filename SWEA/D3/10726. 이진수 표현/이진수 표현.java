import java.util.*;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            
            String answer;
            int mask = (1 << N) - 1;	// 111...1 (길이 N)
            if ((M & mask) == mask) {	// M % mask : M의 마지막 N비트를 얻을 수 있다.
                answer = "ON";
            } else {
                answer = "OFF";
            }
			bw.write("#" + test_case + " " + answer + "\n");
		}
        bw.flush();
        bw.close();
        br.close();
	}
}