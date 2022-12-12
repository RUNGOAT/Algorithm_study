from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in adjL[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.append(w)


N, M = map(int, input().split())
indegree = [0] * (N+1)
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    indegree[b] += 1
bfs()
