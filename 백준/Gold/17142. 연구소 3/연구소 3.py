from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def bfs(q):
    q = deque(q)
    while q:
        x, y = q.popleft()
        for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


def check_time():
    time = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                if visited[x][y] == 0:
                    time = 2501
                elif time < visited[x][y]:
                    time = visited[x][y]
    return time


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2의 위칫값 저장
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))

min_time = 2501
# 조합 3개씩 뽑아서
for comb in combinations(virus, M):

    visited = [[0] * N for _ in range(N)]
    for x, y in comb:
        visited[x][y] = 1
    # bfs
    bfs(comb)

    time = check_time()

    min_time = min(time, min_time)

if min_time == 2501:
    min_time = -1
elif min_time != 0:
    min_time -= 1

# 최소 시간 출력
print(min_time)