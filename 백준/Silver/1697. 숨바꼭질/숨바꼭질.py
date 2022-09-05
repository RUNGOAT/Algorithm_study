import sys
from collections import deque


def bfs(n, k, size):

    visited[n] = 1
    q = deque()
    q.append(N)
    while q:
        n = q.popleft()
        if n == k:
            return
        for i in [1, -1, n]:
            ni = n + i
            if 0 <= ni < size and visited[ni] == 0:
                q.append(ni)
                visited[ni] = visited[n] + 1


N, K = map(int, sys.stdin.readline().split())
size = 100001
visited = [0] * size
bfs(N, K, size)
print(visited[K]-1)
