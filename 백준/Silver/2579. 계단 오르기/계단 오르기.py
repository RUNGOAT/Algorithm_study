import sys

N = int(sys.stdin.readline())
dp = [0] * 301
stairs = [0] * 301
for i in range(1, N+1):
    stairs[i] = int(sys.stdin.readline())

dp[1] = stairs[1]
dp[2] = stairs[2] + stairs[1]

for i in range(3, N+1):
    dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])

print(dp[N])
