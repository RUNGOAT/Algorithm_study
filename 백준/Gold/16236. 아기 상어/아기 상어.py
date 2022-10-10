from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx, sy):
    global ans, baby, eat
    q = deque([[sx, sy]])
    feed = []
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and baby >= arr[nx][ny] and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if baby > arr[nx][ny] and arr[nx][ny] != 0:
                    feed.append([nx, ny, visited[x][y]])

    if feed:
        feed.sort(key=lambda x: (x[2], x[0], x[1]))
        x, y = feed[0][0], feed[0][1]
        arr[x][y] = 0
        ans += feed[0][2]
        eat += 1
        if eat == baby:
            baby += 1
            eat = 0
        bfs(x, y)
    else:
        print(ans)
        exit(0)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
baby = 2
ans = eat = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            bfs(i, j)
