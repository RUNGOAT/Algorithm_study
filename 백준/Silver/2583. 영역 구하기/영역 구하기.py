import sys
input = sys.stdin.readline


def bfs(x, y):
    cnt = 1
    stack = [[x, y]]
    arr[x][y] = 0
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny]:
                cnt += 1
                stack.append([nx, ny])
                arr[nx][ny] = 0
    return cnt


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
M, N, K = map(int, input().split())
arr = [[1] * N for _ in range(M)]
for _ in range(K):
    sj, si, ej, ei = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = 0

ans = 0
area = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            ans += 1
            area.append(bfs(i, j))
area.sort()
print(ans)
print(' '.join(map(str, area)))
