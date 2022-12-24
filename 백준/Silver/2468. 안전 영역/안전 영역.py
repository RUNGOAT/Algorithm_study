import sys
input = sys.stdin.readline


def soaked_city(rain):
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                visited[i][j] = True


def bfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for nx, ny in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for rain in range(101):
    visited = [[False] * N for _ in range(N)]
    soaked_city(rain)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1

    ans = max(ans, cnt)

print(ans)
