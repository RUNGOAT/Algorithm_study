import heapq
import sys
input = sys.stdin.readline


def bfs2(x, y, v):
    q = [(v, x, y)]
    visited = [[0] * N for _ in range(M)]
    visited[x][y] = 1
    while q:
        v, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and v < arr[nx][ny]:
                if not visited[nx][ny]:
                    heapq.heappush(q, (arr[nx][ny], nx, ny))
                visited[nx][ny] += visited[x][y]
    return visited[0][0]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
print(bfs2(M-1, N-1, arr[M-1][N-1]))
