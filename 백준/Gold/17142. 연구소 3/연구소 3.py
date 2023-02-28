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
                    

# bfs 탐색 후 바이러스가 있는 칸의 시간은 체크할 필요없다.
def check_time():
    time = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:  # 빈 칸인 경우
                if visited[x][y] == 0:
                    time = 2501
                elif time < visited[x][y]:      # 빈 칸을 채운 시간 구하기
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
        
    bfs(comb)
    
    # bfs 탐색으로 걸린 시간
    time = check_time()
    
    # 최소 시간
    min_time = min(time, min_time)

if min_time == 2501:    # 빈 칸을 다 채우지 못한 경우
    min_time = -1
elif min_time != 0:     # 0이면 처음부터 빈 칸이 없는 경우
    min_time -= 1       # 방문체크(visited[x][y])를 1부터 시작함으로 -= 1

# 최소 시간 출력
print(min_time)
