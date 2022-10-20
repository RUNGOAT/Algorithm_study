import sys
input = sys.stdin.readline


def dfs(x, y, cnt, ssum):
    global ans
    if ssum + max_v * (4 - cnt) <= ans:
        return
    if cnt == 4:
        ans = max(ans, ssum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x, y, cnt + 1, ssum + arr[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, ssum + arr[nx][ny])
            visited[nx][ny] = 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_v = max(map(max, arr))
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0
print(ans)