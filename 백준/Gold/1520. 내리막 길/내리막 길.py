import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
            cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dp[M - 1][N - 1] = 1
print(dfs(0, 0))
