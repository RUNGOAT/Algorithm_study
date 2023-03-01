from itertools import combinations
import sys, copy
input = sys.stdin.readline


def attack(posi):
    attack_near_enemy = [(-1, -1, 11) for _ in range(3)]
    for x in range(N-1, -1, -1):
        for y in range(M):
            if test_arr[x][y] == 1:
                for idx, archer_y in enumerate(posi):
                    diff_d = abs(N - x) + abs(archer_y - y)
                    if diff_d <= D:
                        x1, y1, d1 = attack_near_enemy[idx]
                        if diff_d < d1:
                            attack_near_enemy[idx] = (x, y, diff_d)
                        elif diff_d == d1:
                            if y < y1:
                                attack_near_enemy[idx] = (x, y, diff_d)

    return attack_near_enemy


def remove_enemy(attack_near_enemy):
    cnt = 0
    for x, y, _ in attack_near_enemy:
        if x != -1 and test_arr[x][y] == 1:
            test_arr[x][y] = 0
            cnt += 1
    return cnt


def move():
    global test_arr
    test_arr.pop()
    test_arr = [[0] * M] + test_arr


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
archer_posi = range(M)

ans = 0
for posi in combinations(archer_posi, 3):
    test_arr = copy.deepcopy(arr)
    del_enemy = turn = 0
    while turn != N:
        del_enemy += remove_enemy(attack(posi))
        move()
        turn += 1
    ans = max(ans, del_enemy)

print(ans)