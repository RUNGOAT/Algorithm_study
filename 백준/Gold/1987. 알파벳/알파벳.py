import sys
input = sys.stdin.readline


def dfs(x, y, cnt):
    global ans
    if ans == alpa_cnt:
        return
    if ans < cnt:
        ans = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[arr[nx][ny]]:
            visited[arr[nx][ny]] = True
            dfs(nx, ny, cnt + 1)
            visited[arr[nx][ny]] = False


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(map(lambda x: ord(x) - 65, input().strip())))
    
visited = [False] * 26
visited[arr[0][0]] = True

idx = [False] * 26
for i in range(R):
    for j in range(C):
        if not idx[arr[i][j]]:
            idx[arr[i][j]] = True
alpa_cnt = 0
for i in range(26):
    if idx[i]:
        alpa_cnt += 1

ans = 1
dfs(0, 0, 1)
print(ans)
