import sys


def width_check(arr):
    global cnt
    for i in range(5):
        flag = True
        for j in range(5):
            if arr[i][j] != 0:
                flag = False
                break
        if flag:
            cnt += 1


def height_check(arr):
    global cnt
    for i in range(5):
        flag = True
        for j in range(5):
            if arr[j][i] != 0:
                flag = False
                break
        if flag:
            cnt += 1


def diagonal_check_l(arr):
    global cnt
    for i in range(5):
        if arr[i][i] != 0:
            return
    cnt += 1


def diagonal_check_r(arr):
    global cnt
    for i in range(5):
        if arr[i][4-i] != 0:
            return
    cnt += 1


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int, sys.stdin.readline().split()))

for i in range(5):
    for j in range(5):
        if arr[i][j] in nums[:11]:
            arr[i][j] = 0

ans = 0
k = 11
while ans < 3 and k < 25:
    flag = False
    for i in range(5):
        for j in range(5):
            if arr[i][j] == nums[k]:
                arr[i][j] = 0
                cnt = 0
                width_check(arr)
                height_check(arr)
                diagonal_check_l(arr)
                diagonal_check_r(arr)
                ans = cnt
                flag = True
                break
        if flag:
            break
    k += 1
print(k)
