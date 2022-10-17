import sys
input = sys.stdin.readline


N = int(input())
dp = [[0, 0] for _ in range(N+1)]
if N > 2:
    dp[1] = [0, 1]
    dp[2] = [1, 0]
    for i in range(3, N+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    print(sum(dp[N]))
else:
    print(1)
