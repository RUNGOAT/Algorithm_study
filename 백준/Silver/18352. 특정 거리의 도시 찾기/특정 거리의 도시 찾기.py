import sys
input = sys.stdin.readline
from collections import deque


def bfs(x):
    visited = [0] * (N+1)
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        v = q.popleft()
        for w in adjL[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                if visited[v] == K:
                    ans.append(w)
                    continue
                q.append(w)


N, M, K, X = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)

ans = []
bfs(X)
if ans:
    for v in sorted(ans):
        print(v)
else:
    print(-1)
