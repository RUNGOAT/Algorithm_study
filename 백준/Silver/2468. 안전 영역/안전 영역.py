import sys
input = sys.stdin.readline
from collections import  deque


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for k in range(101):
    visited = [[0] * N for _ in range(N)]
    tmp = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k:
                tmp.append([i, j])
            else:
                visited[i][j] = 1

    for x, y in tmp:
        if not visited[x][y]:
            bfs(x, y)
            cnt += 1
    if cnt == 0:
        print(ans)
        exit(0)

    ans = max(ans, cnt)

print(ans)
