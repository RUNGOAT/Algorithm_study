import sys
input = sys.stdin.readline

from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)


def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in adj_list[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
    print()


N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

for i in range(N+1):
    if adj_list[i]:
        adj_list[i].sort()

dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
