import sys
input = sys.stdin.readline


def f():
    tmp = []
    for x, y in ice_list:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] <= 0:
                tmp.append((x, y))

    for x, y in tmp:
        arr[x][y] -= 1

    tmp.clear()
    for x, y in ice_list:
        if arr[x][y] > 0:
            tmp.append((x, y))
    return tmp


def bfs(x, y, ice_size):
    visited = [[False] * M for _ in range(N)]
    stack = [(x, y)]
    visited[x][y] = True
    ice_size -= 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                ice_size -= 1
    if ice_size != 0:
        return True
    return False


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ice_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            ice_list.append((i, j))

year = 0
while True:
    year += 1
    ice_list = f()
    if not ice_list:
        print(0)
        break
    x, y = ice_list[0]
    if bfs(x, y, len(ice_list)):
        print(year)
        break
