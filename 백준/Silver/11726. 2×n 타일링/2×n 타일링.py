import sys

n = int(sys.stdin.readline())

dp = [1, 1]
for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n] % 10007)
