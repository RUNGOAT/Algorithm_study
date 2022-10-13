from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    while q:
        x, y, z = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
                if arr[nx][ny] == 1 and z == 0 :
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(bfs(0, 0, 0))
