import sys


def bfs(i, j):
    q = []
    q.append((i, j))
    cnt = 1
    arr[i][j] = 0
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        # visit()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                cnt += 1
                visited[ni][nj] = 1
                arr[ni][nj] = 0
    return cnt


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = 0
result = []

for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            result.append(bfs(x, y))
            ans += 1

print(ans)
for num in sorted(result):
    print(num)
