N = int(input())
P = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += P[i] * (N-i)
print(ans)
