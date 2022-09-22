import sys
read = sys.stdin.readline


def solve(idx):
    if idx == len(zero_list):
        for i in range(9):
            print(' '.join(map(str, arr[i])))
        exit(0)

    for num in range(1, 10):
        x = zero_list[idx][0]
        y = zero_list[idx][1]
        if width(x, y, num) and vertical(x, y, num) and square3(x, y, num):
            arr[x][y] = num
            solve(idx+1)
            arr[x][y] = 0


def width(x, y, num):
    for j in range(9):
        if num == arr[x][j]:
            return False
    return True


def vertical(x, y, num):
    for i in range(9):
        if num == arr[i][y]:
            return False
    return True


def square3(x, y, num):
    if x < 3:
        tmp_x = 0
    elif x < 6:
        tmp_x = 3
    else:
        tmp_x = 6

    if y < 3:
        tmp_y = 0
    elif y < 6:
        tmp_y = 3
    else:
        tmp_y = 6

    for i in range(tmp_x, tmp_x + 3):
        for j in range(tmp_y, tmp_y + 3):
            if num == arr[i][j]:
                return False
    return True


arr = [list(map(int, read().split())) for _ in range(9)]
zero_list = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_list.append([i, j])

solve(0)
