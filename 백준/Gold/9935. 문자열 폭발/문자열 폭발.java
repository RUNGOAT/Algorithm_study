import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main
{
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String bam = br.readLine();
        
        Stack<Character> stack = new Stack<>();  
        
        for (int i = 0; i < str.length(); i++) {
        	stack.push(str.charAt(i));
        	int stackSize = stack.size();
        	int bamLength = bam.length();
        	if (stackSize >= bamLength) {
        		boolean isSame = true;
        		for (int j = 0; j < bam.length(); j++) {
        			if (stack.get(stackSize - bamLength + j) != bam.charAt(j)) {
        				isSame = false;
        				break;
        			}
        		}
        		
        		if (isSame) {
        			for (int j = 0; j < bamLength; j++) {
        				stack.pop();
        			}
        		}
        	}
        }
        
        StringBuilder sb = new StringBuilder();
        for (char ch : stack) {
        	sb.append(ch);
        }
        
		System.out.println(sb.length() == 0 ? "FRULA" : sb.toString());
	}
}