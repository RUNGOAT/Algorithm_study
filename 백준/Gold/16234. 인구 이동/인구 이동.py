import sys
input = sys.stdin.readline


def bfs(x, y):
    global flag
    stack = [(x, y)]
    visited[x][y] = union_idx
    cnt = 1
    po_sum = arr[x][y]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                cnt += 1
                po_sum += arr[nx][ny]
                stack.append((nx, ny))
                visited[nx][ny] = union_idx
    if cnt != 1:
        flag = False
    return po_sum // cnt


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, L, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

date = 0
visited = [[0] * N for _ in range(N)]
while True:
    union_po = [0]
    union_idx = 1
    flag = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union_po.append(bfs(i, j))
                union_idx += 1
    if flag:
        print(date)
        break
    for i in range(N):
        for j in range(N):
            arr[i][j] = union_po[visited[i][j]]
            visited[i][j] = 0
    date += 1
