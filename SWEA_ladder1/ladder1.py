import sys
sys.stdin = open('사다리.txt')

tc = int(input())
N = 100
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, 0]  # 아래 왼쪽 오른쪽
dj = [0, -1, 1]

for j in range(N):
    if arr[0][j] == 1:
        result = j
        i = 0
        # j += dj[0]
        while i < N:
            i += di[0]
            j += dj[0]
            if 0 <= i < N and 0 <= j+dj[1] and j+dj[2] < N:
                if arr[i+di[1]][j+dj[1]] == 1:      # 왼쪽
                    i += di[1]
                    j += dj[1]
                elif arr[i+di[2]][j+dj[2]] == 1:    # 오른쪽
                    i += di[2]
                    j += dj[2]
                # else:           # 아래
                #     i += di[0]
                #     j += dj[0]
            else:
                i += di[0]
                j += dj[0]

        if arr[i-1][j] == 2:
            print(f'#{tc} {result}')
            break
