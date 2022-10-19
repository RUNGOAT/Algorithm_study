import sys
input = sys.stdin.readline

N = int(input())
box = list(map(int, input().split()))
dp = [1] * N
for i in range(N-1):
    for j in range(i+1, N):
        if box[i] < box[j]:
            dp[j] = max(dp[i] + 1, dp[j])
print(max(dp))
