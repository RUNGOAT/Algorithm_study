from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, k):
    q = deque()
    q.append(n)
    visited = [True] * MAX
    dist = [-1] * MAX
    visited[n] = False
    dist[n] = 0
    while q:
        n = q.popleft()
        if n * 2 < MAX and visited[n*2]:
            visited[n*2] = False
            dist[n*2] = dist[n]
            q.appendleft(n * 2)
        if n - 1 >= 0 and visited[n - 1]:
            visited[n - 1] = False
            dist[n - 1] = dist[n] + 1
            q.append(n - 1)
        if n + 1 < MAX and visited[n + 1]:
            visited[n + 1] = False
            dist[n + 1] = dist[n] + 1
            q.append(n + 1)
    return dist[k]


MAX = 100001
N, K = map(int, input().split())
print(bfs(N, K))