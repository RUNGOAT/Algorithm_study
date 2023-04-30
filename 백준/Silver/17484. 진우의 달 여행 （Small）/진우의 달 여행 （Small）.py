import sys
input = sys.stdin.readline


def dfs(x, y, dd, fuel):
    global ans
    if x == N-1:
        ans = min(ans, fuel)
        return
    for d in range(3):
        if d == dd: continue
        ny = y + dy[d]
        if 0 <= ny < M:
            dfs(x+1, ny, d, fuel + arr[x+1][ny])


dy = (-1, 0, 1)
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 601

for j in range(M):
    dfs(0, j, 0, arr[0][j])
    dfs(0, j, 1, arr[0][j])
    dfs(0, j, 2, arr[0][j])

print(ans)
