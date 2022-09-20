def f(idx, cnt):
    if cnt == M:
        print(' '.join(map(str, tmp)))
    else:
        for i in range(idx, N+1):
            tmp.append(i)
            f(i, cnt + 1)
            tmp.pop()


N, M = map(int, input().split())
tmp = []
f(1, 0)
