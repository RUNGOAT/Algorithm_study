def f(cnt):
    if cnt == M:
        print(*temp)
        return
    else:
        for i in range(N):
            if num_list[i] not in temp:
                temp.append(num_list[i])
                f(cnt + 1)
                temp.pop()


N, M = map(int, input().split())
num_list = list(range(1, N+1))
temp = []
f(0)
