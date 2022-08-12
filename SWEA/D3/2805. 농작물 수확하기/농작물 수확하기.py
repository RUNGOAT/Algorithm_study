T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    total = 0

    for i in range(mid):
        for j in range(mid-i, mid+i+1):
            total += arr[i][j]

    for i in range(N):
        total += arr[mid][i]

    for i in range(1, mid+1):
        for j in range(i, N-i):
            total += arr[mid+i][j]

    print(f'#{tc} {total}')
