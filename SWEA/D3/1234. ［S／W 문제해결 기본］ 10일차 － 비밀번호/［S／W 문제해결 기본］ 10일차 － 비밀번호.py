def new_list(lst, x, y):
    temp = []
    for i in range(len(lst)):
        if i != x and i != y:
            temp.append(lst[i])
    return temp


for tc in range(1, 11):
    N, nums = input().split()
    N = int(N)
    secret = list(map(int, nums))

    play = True
    while play:
        for i in range(len(secret)-1):
            if secret[i] == secret[i+1]:
                secret = new_list(secret, i, i+1)
                break
        else:
            play = False

    print(f'#{tc}', end=' ')
    print(*secret, sep='')
