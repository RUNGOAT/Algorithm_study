import sys
sys.stdin = open('사다리.txt')


for _ in range(1, 11):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, 0]  # 아래 왼쪽 오른쪽
    dj = [0, -1, 1]
    # print(arr[99][57])
    for j in range(N):
        if arr[0][j] == 1:
            result = j
            # i = di[0]
            # j += dj[0]
            i = 0
            d = 0
            ni = 0
            while ni < N-1:
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                    i = ni
                    j = nj
                    if j + dj[1] != -1 and arr[i+di[1]][j+dj[1]] == 1 and d == 0:
                        # if arr[i+di[1]][j+dj[1]] == 1:      # 왼쪽
                        d = 1
                    elif j+dj[2] != N and arr[i+di[2]][j+dj[2]] == 1 and d == 0:
                        # if arr[i+di[2]][j+dj[2]] == 1:    # 오른쪽
                        d = 2
                else:
                    d = 0
            else:
                i = 99

            if arr[i][j] == 2:
                print(f'#{tc} {result}')
                break