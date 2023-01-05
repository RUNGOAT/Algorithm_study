from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for w in adjL[v]:
            if not visited[w]:
                visited[w] = -1 * visited[v]
                q.append(w)
            elif visited[w] == visited[v]:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adjL[u].append(v)
        adjL[v].append(u)
    visited = [0] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            result = bfs(i)
            if not result:
                break
    print('YES' if result else 'NO')
