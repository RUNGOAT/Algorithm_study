def f(idx, cnt):
    if cnt == M:
        print(*temp)
        return
    else:
        for i in range(idx, N):
            temp.append(num_list[i])
            f(i+1, cnt + 1)
            temp.pop()


N, M = map(int, input().split())
num_list = list(range(1, N+1))
temp = []
f(0, 0)
