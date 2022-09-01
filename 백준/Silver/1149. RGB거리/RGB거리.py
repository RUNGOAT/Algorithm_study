import sys

N = int(sys.stdin.readline())

dp = []
for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

for n in range(1, N):
    dp[n][0] += min(dp[n-1][1], dp[n-1][2])
    dp[n][1] += min(dp[n-1][0], dp[n-1][2])
    dp[n][2] += min(dp[n-1][0], dp[n-1][1])

print(min(dp[N-1]))
