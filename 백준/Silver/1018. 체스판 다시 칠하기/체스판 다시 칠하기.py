import sys


def chess_num_W(x, y):
    cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8, 2):
            if arr[i][j] != stone[0]:
                cnt += 1
            if arr[i][j+1] != stone[1]:
                cnt += 1
        stone.reverse()
    return cnt


def chess_num_B(x, y):
    cnt = 0
    stone.reverse()
    for i in range(x, x+8):
        for j in range(y, y+8, 2):
            if arr[i][j] != stone[0]:
                cnt += 1
            if arr[i][j+1] != stone[1]:
                cnt += 1
        stone.reverse()
    return cnt


N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]

ans = 2500
stone = ["W", "B"]
for i in range(N-8+1):
    for j in range(M-8+1):
        ans = min(ans, chess_num_W(i, j), chess_num_B(i, j))
        stone.reverse()

print(ans)
