import sys
input = sys.stdin.readline

A = int(input())
sequence = list(map(int, input().split()))
dp = [[1, 1] for _ in range(A)]

for i in range(A-1, -1, -1):
    for j in range(i+1, A):
        if sequence[i] > sequence[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        if sequence[i] < sequence[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1)

print(max(max([dp[x][0] for x in range(A)]), max([dp[x][1] for x in range(A)])))
