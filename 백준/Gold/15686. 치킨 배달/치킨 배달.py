import sys
read = sys.stdin.readline
from collections import deque
from itertools import combinations


def bfs():
    global cnt, distance, min_distance
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == 1:
                    cnt += 1
                    distance += visited[i][j]
                    if cnt == home:
                        min_distance = min(min_distance, distance)
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


N, M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]

home = 0
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home += 1
        elif arr[i][j] == 2:
            chickens.append([i, j])

q = deque()
min_distance = 999999999
for tmp in combinations(chickens, M):
    cnt = distance = 0
    visited = [[0] * N for _ in range(N)]
    for m in tmp:
        q.append(m)
        visited[m[0]][m[1]] = 1
    bfs()

print(min_distance)
