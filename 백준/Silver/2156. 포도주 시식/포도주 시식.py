import sys
input = sys.stdin.readline

N = int(input())
wine = [0] * N
dp = [0] * N
for n in range(N):
    wine[n] = int(input())
dp = [0] * N
if N < 3:
    print(sum(wine))
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(max(wine[0], wine[1]) + wine[2], dp[1])

    for i in range(3, N):
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

    print(dp[N-1])
