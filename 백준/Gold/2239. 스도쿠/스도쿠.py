def check(x, y, k):
    if k in arr[x]:
        return False

    for i in range(9):
        if k == arr[i][y]:
            return False

    h = 3 * (x // 3)
    w = 3 * (y // 3)
    for i in range(h, h+3):
        for j in range(w, w+3):
            if k == arr[i][j]:
                return False
    return True


def sudoku(idx):
    if idx == zero_cnt:
        for i in range(9):
            print(''.join(map(str, arr[i])))
        exit(0)

    x, y = zero_posi[idx]
    for k in range(1, 10):
        if check(x, y, k):
            arr[x][y] = k
            sudoku(idx+1)
            arr[x][y] = 0


arr = [list(map(int, input())) for _ in range(9)]
zero_posi = []
zero_cnt = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_posi.append((i, j))
            zero_cnt += 1
sudoku(0)
