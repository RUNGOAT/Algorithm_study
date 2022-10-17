import sys
input = sys.stdin.readline


N = int(input())
T = [0] * (N+1)
P = [0] * (N+1)
dp = [0] * (N+2)

for n in range(1, N+1):
    t, p = map(int, input().split())
    T[n] = t
    P[n] = p

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    if i + T[i] <= N+1:
        dp[i + T[i]] = max(dp[i+T[i]], dp[i] + P[i])
print(max(dp[N], dp[N+1]))
