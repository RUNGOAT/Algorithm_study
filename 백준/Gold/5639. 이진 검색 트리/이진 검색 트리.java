import java.util.*;
import java.io.*;


class Node {
	int data;
	Node left, right;
	
	Node(int data) {
		this.data = data;
	}
}

class Tree {
	Node root;
	
	void createNode(int data) {
		if (root == null) {
			root = new Node(data);
		} else {
			searchNode(root, data);
		}
	}
	
	void searchNode(Node node, int data) {
		if (node.data > data) {
	        	if (node.left == null) {
	            		node.left = new Node(data);
	        	} else {
	        		searchNode(node.left, data);				
	        } else {
	        	if (node.right == null) {
	            		node.right = new Node(data);
	        	} else {
	        		searchNode(node.right, data);				
	        	}
	    	}
	}
	
	void postOrder(Node node) {
		if (node != null) {
			postOrder(node.left);
			postOrder(node.right);
			System.out.println(node.data);
		}
	}
}


public class Main {

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	Tree tree = new Tree();
    	String input;
    	while ((input = br.readLine()) != null && !input.isEmpty()) {
    		int data = Integer.parseInt(input);
        	tree.createNode(data);
    	}
    	tree.postOrder(tree.root);
    }
}
