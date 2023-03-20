import sys, copy
input = sys.stdin.readline


def spread_dust(x, y, dust):
    spread_flag = []
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
            spread_flag.append((nx, ny))
    spread = dust // 5
    for nx, ny in spread_flag:
        arr[nx][ny] += spread
        arr[x][y] -= spread


def air_cleaner(x, y, dir):
    dir_x = [d * dir for d in dx]
    d = 0
    dust = 0
    while True:
        nx, ny = x + dir_x[d], y + dy[d]
        if not (0 <= nx < R and 0 <= ny < C):
            d = (d+1) % 4
            nx, ny = x + dir_x[d], y + dy[d]

        next_dust = arr[nx][ny]
        if next_dust == -1:
            return
        arr[nx][ny] = dust
        dust = next_dust
        x, y = nx, ny


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

for r in range(2, R):
    if arr[r][0] == -1:
        cleaner_up_posi, cleaner_down_posi = r, r+1
        break

for _ in range(T):

    # 1. 미세먼지 확산
    dust_list = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                dust_list.append((r, c, arr[r][c]))
    for r, c, dust in dust_list:
        spread_dust(r, c, dust)

    # 2. 공기청정기 작동
    air_cleaner(cleaner_up_posi, 0, 1)
    air_cleaner(cleaner_down_posi, 0, -1)

print(sum([sum(arr[r]) for r in range(R)]) + 2)
