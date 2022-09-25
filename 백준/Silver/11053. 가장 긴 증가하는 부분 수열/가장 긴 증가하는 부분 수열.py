import sys
input = sys.stdin.readline

A = int(input())
sequence = list(map(int, input().split()))
dp = [1] * A
for i in range(A-1, -1, -1):
    min_idx = i
    for j in range(i + 1, A):
        if sequence[min_idx] < sequence[j]:
            dp[min_idx] = max(dp[min_idx], dp[j] + 1)

print(max(dp))
