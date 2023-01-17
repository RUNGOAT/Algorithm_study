import sys
input = sys.stdin.readline


def bfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                stack.append((nx, ny))
                if nx == M-1:
                    print('YES')
                    exit(0)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
for n in range(N):
    if arr[0][n] == 0 and not visited[0][n]:
        bfs(0, n)
print('NO')
