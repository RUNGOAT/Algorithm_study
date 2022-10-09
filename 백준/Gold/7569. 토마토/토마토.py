from collections import deque
import sys
input = sys.stdin.readline


def bfs(q):
    while q:
        k, x, y = q.popleft()
        for dk, dx, dy in d:
            nk = k + dk
            nx = x + dx
            ny = y + dy
            if 0 <= nk < H and 0 <= nx < N and 0 <= ny < M and arr[nk][nx][ny] == 0:
                q.append([nk, nx, ny])
                arr[nk][nx][ny] = arr[k][x][y] + 1


d = [[1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0]]
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
flag = True
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                q.append([k, i, j])
            elif arr[k][i][j] == 0:
                flag = False
if flag:
    print(0)
    exit(0)
bfs(q)

ans = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                print(-1)
                exit(0)
            elif ans < arr[k][i][j]:
                ans = arr[k][i][j]

print(ans - 1)
