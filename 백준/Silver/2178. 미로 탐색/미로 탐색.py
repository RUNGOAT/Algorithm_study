import sys
input = sys.stdin.readline
from collections import deque


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append([ni, nj])
                visited[ni][nj] = visited[x][y] + 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs(0, 0)
print(visited[N-1][M-1])
