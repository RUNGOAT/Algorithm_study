T = int(input())

for _ in range(T):
    ps = list(input())
    cnt = 0
    for p in ps:
        if p == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            print('NO')
            break
    else:
        if cnt == 0:
            print('YES')
        else:
            print('NO')
