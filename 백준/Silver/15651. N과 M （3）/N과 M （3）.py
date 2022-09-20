def f(cnt):
    if cnt == M:
        print(' '.join(map(str, tmp)))
    else:
        for i in range(1, N+1):
            tmp.append(i)
            f(cnt + 1)
            tmp.pop()


N, M = map(int, input().split())
tmp = []
f(0)
