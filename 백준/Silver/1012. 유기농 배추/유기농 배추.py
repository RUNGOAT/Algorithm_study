import sys


def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    arr[i][j] = 0
    while q:
        i, j = q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                arr[ni][nj] = 0


T = int(sys.stdin.readline())
for _ in range(1, T+1):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        Y, X = map(int, sys.stdin.readline().split())
        arr[X][Y] = 1

    ans = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                bfs(x, y)
                ans += 1

    print(ans)
