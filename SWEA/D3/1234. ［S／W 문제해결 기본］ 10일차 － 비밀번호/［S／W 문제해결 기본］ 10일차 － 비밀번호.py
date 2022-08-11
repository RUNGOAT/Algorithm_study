for tc in range(1, 11):
    N, nums = input().split()
    N = int(N)
    secret = list(map(int, nums))

    for x in range(N // 2):
        N = len(secret)
        temp = []
        i = 0
        while i < N-1:
            if secret[i] != secret[i+1]:
                temp.append(secret[i])
            else:
                i += 1
            i += 1
            if i == N - 1:
                temp.append(secret[i])
        secret = temp

    print(f'#{tc}', end=' ')
    print(*secret, sep='')
    