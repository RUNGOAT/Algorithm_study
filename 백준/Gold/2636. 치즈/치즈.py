import sys
input = sys.stdin.readline


def bfs(stack):
    set_arr = set()
    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        for nx, ny in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    set_arr.add((nx, ny))
                else:
                    stack.append((nx, ny))

    for x, y in set_arr:
        arr[x][y] = 0
        del cheeze[(x, y)]
    return list(set_arr)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 치즈 위칫값 저장
cheeze = {}
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheeze[(i, j)] = (i, j)

time = 0
ans = len(cheeze)
tmp = [(0, 0)]
visited = [[False] * M for _ in range(N)]
while True:
    time += 1
    tmp = bfs(tmp)
    len_cheeze = len(cheeze)
    if len_cheeze == 0:
        print(time)
        print(ans)
        break
    ans = len_cheeze
