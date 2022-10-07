import sys
input = sys.stdin.readline


N = int(input())
dp = [0] * (N+1)
dp[0], dp[1] = 0, 1
for i in range(2, N+1):
    min_v = 4
    j = 1
    while j**2 <= i:
        min_v = min(min_v, dp[i - j**2])
        j += 1
    dp[i] = min_v + 1

print(dp[N])
