import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
q = deque()
arr = [[0] * N for _ in range(N)]
for k in range(K):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1][j-1] = 1
L = int(sys.stdin.readline())
direction = []
for _ in range(L):
    s, l = map(str, sys.stdin.readline().split())
    direction.append([int(s), l])
direction.append([-1, -1])
q.append([0, 0])
sec = 0
idx = 0
di = 0
dj = 1
i = j = 0

while q:

    ni = i + di
    nj = j + dj
    i, j = ni, nj

    # 변수 위에서 설정하고 와야 함
    if 0 <= ni < N and 0 <= nj < N and [ni, nj] not in q:
        q.append([ni, nj])
        # arr[ni][nj] = 2
        if arr[ni][nj] == 0:
            q.popleft()
        elif arr[ni][nj] == 1:
            arr[ni][nj] = 0
    else:
        print(sec + 1)
        break

    sec += 1

    if sec == direction[idx][0]:
        if di == 0 and dj == 1:
            if direction[idx][1] == 'L':
                di, dj = -1, 0
            else:
                di, dj = 1, 0

        elif di == -1 and dj == 0:
            if direction[idx][1] == 'L':
                di, dj = 0, -1
            else:
                di, dj = 0, 1

        elif di == 0 and dj == -1:
            if direction[idx][1] == 'L':
                di, dj = 1, 0
            else:
                di, dj = -1, 0

        elif di == 1 and dj == 0:
            if direction[idx][1] == 'L':
                di, dj = 0, 1
            else:
                di, dj = 0, -1

        idx += 1

