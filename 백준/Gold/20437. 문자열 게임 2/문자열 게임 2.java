import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

class Node {
	int cnt, shortSize, longSize;
	List<Integer> idxList;
	
	public Node () {
		this.cnt = 0;
		idxList = new ArrayList<>();
		shortSize = Integer.MAX_VALUE;
		longSize = 0;
	}
}

public class Main
{
	static final int INF = Integer.MAX_VALUE;
	
    public static void main(String args[]) throws IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	int T = Integer.parseInt(br.readLine());
    	for (int t = 0; t < T; t++) {
    		Node[] alphabet = new Node[26];
    		for (int i = 0; i < 26; i++) {
    			alphabet[i] = new Node();
    		}
    		int shortAnswer = INF;
    		int longAnswer = 0;
    		
    		String W = br.readLine();
    		int K = Integer.parseInt(br.readLine());
    		
    		for (int i = 0; i < W.length(); i++) {
    			char word = W.charAt(i);
    			Node node = alphabet[word - 'a'];
    			node.idxList.add(i);
    			if (++node.cnt >= K) {
    				int size = i - node.idxList.get(node.cnt - K) + 1;
    				node.shortSize = Math.min(node.shortSize, size);
    				node.longSize = Math.max(node.longSize, size);
    			}
    		}
    		
    		for (int i = 0; i < 26; i++) {
    			Node node = alphabet[i];
    			shortAnswer = Math.min(shortAnswer, node.shortSize);
    			longAnswer = Math.max(longAnswer, node.longSize);
    		}
    		
    		if (shortAnswer == INF || longAnswer == 0) {
    			bw.write(-1 + "\n");
    		} else {
    			bw.write(shortAnswer + " " + longAnswer + "\n");
    		}
    	}
    	
    	bw.flush();
    	bw.close();
    	br.close();
    }
}
