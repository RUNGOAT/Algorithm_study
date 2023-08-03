import java.util.*;
import java.io.*;


public class Main
{

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        String secret = br.readLine();

        String buttons = br.readLine();

        if (buttons.contains(secret)) {
            System.out.println("secret");
        } else {
            System.out.println("normal");
        }
    }
}
