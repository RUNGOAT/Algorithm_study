from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append(x)
    visited = [0] * (N+1)
    visited[x] = 1
    while q:
        x = q.popleft()
        for y in adjL[x]:
            if not visited[y]:
                if y == Y:
                    return visited[x]
                q.append(y)
                visited[y] = visited[x] + 1
    return -1


N = int(input())
X, Y = map(int, input().split())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adjL[x].append(y)
    adjL[y].append(x)

print(bfs(X, Y))
