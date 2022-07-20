T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # S_N == Snail_Number
    S_N = [[0 for x in range(N)] for y in range(N)]
    snail = 1

    i = 0
    while True:
        for j in range(i, N-i):
            S_N[i][j] = snail
            snail += 1
        for j in range(i+1, N-i):
            S_N[j][N-1-i] = snail
            snail += 1
        for j in range(N-1-i, i, -1):
            S_N[N-1-i][j-1] = snail
            snail += 1
        for j in range(N-1-i, i + 1, -1):
            S_N[j-1][i] = snail
            snail += 1

        if snail > N*N:
            break
        i += 1

    print(f'#{t}')
    for i in range(len(S_N)):
        for x in S_N[i]:
            print(x, end=" ")
        print()
