import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * LinkedList 구현
 */

class Node {
	int idx;
	Node next;
	
	public Node() {};
	
	public Node(int idx) {
		this.idx = idx;
	}
}

class Alphabet {
	int cnt, shortSize, longSize;
	Node head;
	Node tail;
	
	public Alphabet () {
		this.cnt = 0;
		this.shortSize = Integer.MAX_VALUE;
		this.longSize = 0;
		this.head = this.tail = new Node();
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
    		Alphabet[] alphabet = new Alphabet[26];
    		for (int i = 0; i < 26; i++) {
    			alphabet[i] = new Alphabet();
    		}
    		
    		int shortAnswer = INF;
    		int longAnswer = 0;
    		
    		String W = br.readLine();
    		int K = Integer.parseInt(br.readLine());
    		
    		for (int i = 0; i < W.length(); i++) {
    			char word = W.charAt(i);
    			Alphabet alpha = alphabet[word - 'a'];
    			Node newNode = new Node(i);
    			alpha.tail.next = newNode;
    			alpha.tail = newNode;
    			alpha.cnt++;
    			
    			if (alpha.cnt == K) {
    				int size = alpha.tail.idx - alpha.head.next.idx + 1;
    				
    				alpha.shortSize = Math.min(alpha.shortSize, size);
    				alpha.longSize = Math.max(alpha.longSize, size);
    				
    				if (alpha.head.next.next == null) {
    					alpha.head = alpha.tail = new Node();
    				} else {
    					alpha.head.next = alpha.head.next.next;    					
    				}
    				alpha.cnt--;
    			}
    		}
    		
    		for (int i = 0; i < 26; i++) {
    			Alphabet alpha = alphabet[i];
    			shortAnswer = Math.min(shortAnswer, alpha.shortSize);
    			longAnswer = Math.max(longAnswer, alpha.longSize);
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
