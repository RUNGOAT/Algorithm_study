dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
for i in range(4, 41):
    dp[i][0] += dp[i-1][0] + dp[i-2][0]
    dp[i][1] += dp[i-1][1] + dp[i-2][1]

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    print(dp[N][0], dp[N][1])
    