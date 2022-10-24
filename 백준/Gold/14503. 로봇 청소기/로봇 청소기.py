import sys
input = sys.stdin.readline


def can_go(x, y):
    return 0 <= x < N and 0 <= y < M and arr[x][y] != 1 and arr[x][y] != 2


def is_wall(x, y):
    return 0 == x or x == N - 1 or 0 == y or y == M - 1 or arr[x][y] == 1


def search(x, y, d):
    for i in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if can_go(nx, ny):
            return nx, ny, d
    return -1, -1, -1


def back(x, y, d):
    bd = (d + 2) % 4
    nx = x + dx[bd]
    ny = y + dy[bd]
    if is_wall(nx, ny):
        return -1, -1, -1
    return nx, ny, d


def simulate(x, y, d):
    ans = 0
    while (x, y, d) != EMPTY:
        ans += 1
        # 1. 청소
        arr[x][y] = 2
        # 2. 탐색
        while (x, y, d) != EMPTY:
            nx, ny, nd = search(x, y, d)
            if (nx, ny, nd) == EMPTY:
                x, y, d = back(x, y, d)
            else:
                x, y, d = nx, ny, nd
            if arr[x][y] == 0:
                break

    return ans


EMPTY = (-1, -1, -1)
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(simulate(r, c, d))
