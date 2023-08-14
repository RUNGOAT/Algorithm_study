import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;

public class Main
{
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	int N = Integer.parseInt(br.readLine());
    	LinkedList<Integer> list = new LinkedList<>();
    	for (int i = 1; i <= N; i++) {
    		list.add(i);
    	}
    	
    	while (list.size() != 1 ) {
    		list.pollFirst();
    		list.addLast(list.pollFirst());
    	}
    	
    	bw.write(list.poll() + "\n");
    	bw.flush();
    	bw.close();
    	br.close();
    }
}