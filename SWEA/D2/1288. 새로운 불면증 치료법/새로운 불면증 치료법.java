import java.util.*;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T;
		T=Integer.parseInt(br.readLine());
        
		int all = (1 << 10) - 1;
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = Integer.parseInt(br.readLine());
            int chk = 0;
            
            for (int k = 1; ; k++) {
				int num = k * N;
				
				while (num > 0) {
					int digit = num % 10;
					chk |= 1 << digit;
					num /= 10;
				}
				
				if (chk == all) {
					bw.write("#" + test_case + " " + k * N + "\n");
					break;
				}
			}
		}
        bw.flush();
        bw.close();
        br.close();
	}
}