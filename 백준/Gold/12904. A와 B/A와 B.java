import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main
{
	
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringBuilder S = new StringBuilder(br.readLine());
        StringBuilder T = new StringBuilder(br.readLine());
        
        while (S.length() < T.length()) {
        	if (T.charAt(T.length() - 1) == 'A') {
        		T.deleteCharAt(T.length() - 1);
        	} else {        		
        		T.deleteCharAt(T.length() - 1);
        		T.reverse();
        	}
        }
        
        if (S.toString().equals(T.toString())) {
        	bw.write(1 + "\n");
        } else {
        	bw.write(0 + "\n");
        }
        bw.flush();
		bw.close();
		br.close();
	}
}