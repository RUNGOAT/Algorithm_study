import sys
input = sys.stdin.readline


def dfs(x, y, cnt, ssum):
    global ans
    if cnt == 4:
        ans = max(ans, ssum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            tmp = arr[nx][ny]
            arr[nx][ny] = 0
            dfs(nx, ny, cnt + 1, ssum + tmp)
            arr[nx][ny] = tmp


def ㅗ(x, y, cnt, ssum):
    min_v = 1000
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            cnt += 1
            ssum += arr[nx][ny]
            min_v = min(min_v, arr[nx][ny])
    if cnt == 5:
        ssum -= min_v
    elif cnt < 4:
        return 0
    return ssum


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        tmp = arr[i][j]
        arr[i][j] = 0
        dfs(i, j, 1, tmp)
        arr[i][j] = tmp
        ans = max(ans, ㅗ(i, j, 1, tmp))

print(ans)
