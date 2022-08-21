import sys

C, R = map(int, sys.stdin.readline().split())
arr = [[0] * C for _ in range(R)]
K = int(sys.stdin.readline())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

num = 1
i = R       # 좌측 하단에서 시작
j = 0
d = 0
flag = True
while K <= C * R:
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
        i = ni
        j = nj
        arr[i][j] = num
        if num == K:
            print(j+1, R-i)
            flag = False
            break
        num += 1
    else:
        d = (d + 1) % 4

if flag:
    print(0)
