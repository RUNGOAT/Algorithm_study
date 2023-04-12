from collections import deque
import sys
input = sys.stdin.readline


def attack_check():
    power = 5001
    ax = ay = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 0:  continue
            if arr[x][y] < power:
                power = arr[x][y]
                ax, ay = x, y
            elif arr[x][y] == power:
                if attack_time[x][y] > attack_time[ax][ay]:
                    ax, ay = x, y
                elif attack_time[x][y] == attack_time[ax][ay]:
                    if x + y > ax + ay:
                        ax, ay = x, y
                    elif x + y == ax + ay:
                        if y > ay:
                            ay = y
    return ax, ay


def target_check(ax, ay):
    power = -1
    tx = ty = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 0:  continue
            if x == ax and y == ay: continue
            if arr[x][y] > power:
                power = arr[x][y]
                tx, ty = x, y
            elif arr[x][y] == power:
                if attack_time[x][y] < attack_time[tx][ty]:
                    tx, ty = x, y
                elif attack_time[x][y] == attack_time[tx][ty]:
                    if x + y < tx + ty:
                        tx, ty = x, y
                    elif x + y == tx + ty:
                        if y < ty:
                            tx, ty = x, y
    return tx, ty


def laser(ax, ay, tx, ty):
    q = deque()
    q.append((ax, ay, []))  # x, y, route
    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True
    while q:
        x, y, route = q.popleft()
        for d in range(4):
            nx = (x + dx[d]) % N
            ny = (y + dy[d]) % M
            if visited[nx][ny]: continue
            if arr[nx][ny] == 0: continue
            if nx == tx and ny == ty:
                arr[nx][ny] -= point
                for rx, ry in route:    # 경로 추적
                    arr[rx][ry] -= half_point
                    attack[rx][ry] = True
                return True
            tmp_route = route[:]
            tmp_route.append((nx, ny))
            visited[nx][ny] = True
            q.append((nx, ny, tmp_route))

    return False


def shell(ax, ay, tx, ty):
    arr[tx][ty] -= point
    ddx = dx + [1, 1, -1, -1]
    ddy = dy + [-1, 1, -1, 1]
    for d in range(8):
        nx = (tx + ddx[d]) % N
        ny = (ty + ddy[d]) % M
        if nx == ax and ny == ay:   continue
        arr[nx][ny] -= half_point
        attack[nx][ny] = True


def break_check():
    for x in range(N):
        for y in range(M):
            if arr[x][y] < 0:
                arr[x][y] = 0


def max_check():
    return max([max(line) for line in arr])


def turret_check():
    turret = []
    turret_cnt = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 0:  continue
            turret_cnt += 1
            if attack[x][y]:    continue
            turret.append((x, y))

    if turret_cnt == 1:
        print(max_check())
        exit(0)
    for x, y in turret:
        arr[x][y] += 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack_time = [[0] * M for _ in range(N)]  # 공격 시점 배열
time = 1

for k in range(K):
    attack = [[False] * M for _ in range(N)]  # 공격 관련 여부 배열
    
    # 1. 공격자 선정
    attack_i, attack_j = attack_check()
    arr[attack_i][attack_j] += N + M
    point = arr[attack_i][attack_j]
    half_point = point // 2
    attack[attack_i][attack_j] = True
    attack_time[attack_i][attack_j] = time
    time += 1
    

    # 2. 공격자의 공격
    target_i, target_j = target_check(attack_i, attack_j)
    attack[target_i][target_j] = True

    if not laser(attack_i, attack_j, target_i, target_j):
        shell(attack_i, attack_j, target_i, target_j)


    # 3. 포탑 부서짐
    break_check()

    # 4. 포탑 정비
    turret_check()

print(max_check())
