for x in range(int(input())):
    m = list(map(int, input()))
    first_m = [0] * len(m)
    cnt = 0
    for i in range(len(m)):
        if first_m[i] != m[i] and first_m[i] == 0:
            first_m[i:] = [1 for _ in range(len(first_m) - i)]
            cnt += 1
        elif first_m[i] != m[i] and first_m[i] == 1:
            first_m[i:] = [0 for _ in range(len(first_m) - i)]
            cnt += 1

    print(f'#{x+1} {cnt}')