import sys
from collections import deque


def bfs(N, M):
    q = deque()
    flag = True
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
            elif arr[i][j] == 0:
                flag = False

    if flag:
        return 0

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[ni][nj] = arr[i][j] + 1

    ans = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
            if ans < arr[i][j]:
                ans = arr[i][j]
    return ans - 1


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(bfs(N, M))
