T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    num = 1
    i = 0
    while num <= N*N:
        for j in range(i, N-i):
            arr[i][j] = num
            num += 1

        for j in range(i+1, N-i):
            arr[j][N-1-i] = num
            num += 1

        for j in range(N-2-i, i, -1):
            arr[N-1-i][j] = num
            num += 1

        for j in range(N-1-i, i, -1):
            arr[j][i] = num
            num += 1

        i += 1

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
