import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for w in adj[v]:
            if visited[w] == 0:
                q.append(w)
                PI[w] = v
                visited[w] = 1


N = int(input())
adj = [[] for _ in range(N+1)]
PI = list(range(N+1))
visited = [0] * (N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
bfs(1)
for i in range(2, N+1):
    print(PI[i])
