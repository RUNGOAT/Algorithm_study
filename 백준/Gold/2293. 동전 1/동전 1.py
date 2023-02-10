import sys
input = sys.stdin.readline


N, K = map(int, input().split())
coin_list = []
for _ in range(N):
        coin_list.append(int(input()))

dp = [0] * (K+1)
dp[0] = 1

for coin in coin_list:
    for i in range(coin, K+1):
        dp[i] += dp[i - coin]

print(dp[K])