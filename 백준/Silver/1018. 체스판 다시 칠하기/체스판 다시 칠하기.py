import sys
from copy import deepcopy


def chess_num_W():
    cnt = 0
    for i in range(8):
        for j in range(0, 8, 2):
            if temp_arr_W[i][j] != stone[0]:
                temp_arr_W[i][j] = stone[0]
                cnt += 1
            if temp_arr_W[i][j+1] != stone[1]:
                temp_arr_W[i][j+1] = stone[1]
                cnt += 1
        stone.reverse()
    return cnt


def chess_num_B():
    cnt = 0
    stone.reverse()
    for i in range(8):
        for j in range(0, 8, 2):
            if temp_arr_B[i][j] != stone[0]:
                temp_arr_B[i][j] = stone[0]
                cnt += 1
            if temp_arr_B[i][j+1] != stone[1]:
                temp_arr_B[i][j+1] = stone[1]
                cnt += 1
        stone.reverse()
    return cnt


N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]

ans = 2500
stone = ["W", "B"]
for i in range(N-8+1):
    for j in range(M-8+1):
        temp_arr_W = [[] for _ in range(8)]
        for k in range(8):
            temp_arr_W[k] = arr[i+k][j:j+8]
        temp_arr_B = deepcopy(temp_arr_W)
        ans = min(ans, chess_num_W(), chess_num_B())
        stone.reverse()

print(ans)
