import java.util.*;

class Node implements Comparable<Node> {
    int idx, cost;
    
    Node(int idx, int cost) {
        this.idx = idx;
        this.cost = cost;
    }
    
    @Override
    public int compareTo(Node o1) {
        return Integer.compare(this.cost, o1.cost);
    }
}

class Solution {
    
    static List<Node>[] graph;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        
        graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<Node>();
        }
        
        for (int[] fare : fares) {
            graph[fare[0]].add(new Node(fare[1], fare[2]));
            graph[fare[1]].add(new Node(fare[0], fare[2]));
        }
        
        int[] distA = new int[n+1];
        int[] distB = new int[n+1];
        int[] dist = new int[n+1];
        
        Arrays.fill(distA, Integer.MAX_VALUE);
        Arrays.fill(distB, Integer.MAX_VALUE);
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        distA = dijkstra(a, distA);
        distB = dijkstra(b, distB);
        dist = dijkstra(s, dist);
        
        for (int i = 1; i <= n; i++) {
            answer = Math.min(answer, distA[i] + distB[i] + dist[i]);
        }
        
        return answer;
    }
    
    static int[] dijkstra(int start, int[] dist) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        dist[start] = 0;
        
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (dist[now.idx] < now.cost)   continue;
            
            for (Node next : graph[now.idx]) {
                if (dist[next.idx] > now.cost + next.cost) {
                    dist[next.idx] = now.cost + next.cost;
                    pq.offer(new Node(next.idx, dist[next.idx]));
                }
            }
        }
        return dist;
    }
}