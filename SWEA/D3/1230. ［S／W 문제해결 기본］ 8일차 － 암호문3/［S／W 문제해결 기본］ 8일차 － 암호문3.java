import java.util.*;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
		for(int test_case = 1; test_case <= 10; test_case++)
		{
			int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            LinkedList<Integer> list = new LinkedList<>();
            for (int i = 0; i < N; i++) {
             	list.add(Integer.parseInt(st.nextToken()));
            }
            int M = Integer.parseInt(br.readLine());
            
            st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < M; i++) {
				char order = st.nextToken().charAt(0);
                if (order == 'I') {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++) {
                        list.add(x+j, Integer.parseInt(st.nextToken()));
                    }
                } else if (order == 'D') {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++) {
						list.remove(x);   
                    }
                } else {
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++) {
                        list.add(Integer.parseInt(st.nextToken()));
                    }
                }
            }
            
            bw.write("#" + test_case + " ");
            for (int i = 0; i < 10; i++) {
             	bw.write(list.get(i) + " ");
            }
            bw.write("\n");
		}
        bw.flush();
        bw.close();
        br.close();
	}
}