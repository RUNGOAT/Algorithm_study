import sys
input = sys.stdin.readline


def bfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True


dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, 1, 1, -1, -1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit(0)
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)
