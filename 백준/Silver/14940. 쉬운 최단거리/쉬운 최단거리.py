from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * M for _ in range(N)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and arr[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == -1:
                visited[i][j] = 0
            print(visited[i][j], end=" ")
        print()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)
            exit()
