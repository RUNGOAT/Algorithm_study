import sys
input = sys.stdin.readline


def bfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    cnt = 1
    tmp = set()
    while stack:
        x, y = stack.pop()
        for nx, ny in [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]:
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
                else:
                    tmp.add((nx, ny))

    for x, y in tmp:
        arr[x][y] += cnt
        # arr[x][y] %= 10


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not arr[i][j] and not visited[i][j]:
            bfs(i, j)

for i in range(N):
    print(''.join(map(lambda x: str(x % 10), arr[i])))
