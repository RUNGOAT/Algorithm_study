import sys
input = sys.stdin.readline


def dfs(x, y, cnt):
    global ans
    if ans == 26:
        return
    if ans < cnt:
        ans = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(arr[nx][ny]) - 65]:
            visited[ord(arr[nx][ny]) - 65] = True
            dfs(nx, ny, cnt + 1)
            visited[ord(arr[nx][ny]) - 65] = False


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input().strip()))
visited = [False] * 26
visited[ord(arr[0][0]) - 65] = True
ans = 0
dfs(0, 0, 1)
print(ans)
