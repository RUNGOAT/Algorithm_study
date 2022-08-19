N = 4
arr = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(N):
    s1, e1, s2, e2, = map(int, input().split())

    for i in range(s1, s2):
        for j in range(e1, e2):
            arr[i][j] = 1

print(sum(sum(k) for k in arr))
