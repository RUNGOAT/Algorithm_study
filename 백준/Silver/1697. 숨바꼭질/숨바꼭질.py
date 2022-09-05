import sys


def bfs(n, k, size):

    visited[n] = 1
    q = [N]
    while q:
        n = q.pop(0)
        if n == k:
            return
        for i in [1, -1, n]:
            ni = n + i
            if 0 <= ni < size and visited[ni] == 0:
                q.append(ni)
                visited[ni] = visited[n] + 1


N, K = map(int, sys.stdin.readline().split())
size = 200002
visited = [0] * 200002
bfs(N, K, size)
print(visited[K]-1)
