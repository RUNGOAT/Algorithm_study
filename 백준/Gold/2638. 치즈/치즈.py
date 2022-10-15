import sys
input = sys.stdin.readline


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = -1
stack = [[0, 0]]
ans = 0
while True:
    tmp = []
    while stack:
        i, j = stack.pop()
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = -1
                    stack.append([ni, nj])
                elif arr[ni][nj]:
                    visited[ni][nj] += 1
                    if visited[ni][nj] > 1:
                        tmp.append([ni, nj])
                        visited[ni][nj] = -1
    if tmp:
        ans += 1
        for i, j in tmp:
            arr[i][j] = 0
        stack = tmp
    else:
        print(ans)
        exit(0)
