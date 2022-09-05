import sys
from collections import deque
import copy


def bfs():
    global ans
    d_queue = deque(q)
    visited = copy.deepcopy(arr)
    while d_queue:
        i, j = d_queue.popleft()
        visited[i][j] = 2
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                d_queue.append((ni, nj))
                visited[ni][nj] = 2

    cnt = 0
    for i in range(N):
        cnt += visited[i].count(0)

    if ans < cnt:
        ans = cnt


def build_wall(wall):
    if wall == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    build_wall(wall + 1)
                    arr[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            q.append((i, j))

ans = 0
build_wall(0)
print(ans)
