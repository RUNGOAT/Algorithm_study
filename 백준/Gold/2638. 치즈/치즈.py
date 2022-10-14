from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    visited = [[1] * M for _ in range(N)]
    bfs(0, 0)
    tmp = []
    for i in range(N):
        for j in range(M):
            cnt = 0
            if visited[i][j]:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if visited[ni][nj] == 0:
                        cnt += 1
                if cnt > 1:
                    tmp.append([i, j])

    if tmp:
        for i, j in tmp:
            arr[i][j] = 0
        ans += 1
    else:
        print(ans)
        exit(0)
