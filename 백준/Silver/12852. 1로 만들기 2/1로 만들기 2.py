N = int(input())

dp = [0] * 1000001

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])
result = [N]
for _ in range(dp[N]):
    temp = N-1

    if N % 2 == 0 and dp[N // 2] < dp[temp]:
        temp = N // 2
    if N % 3 == 0 and dp[N // 3] < dp[temp]:
        temp = N // 3
    N = temp
    result.append(temp)

print(*result)