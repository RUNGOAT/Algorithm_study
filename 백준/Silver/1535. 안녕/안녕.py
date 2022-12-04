import sys
input = sys.stdin.readline


N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
dp = [0] * 101

for i in range(N):
    energy, pleasure = L[i], J[i]
    for e in range(100, energy, -1):
        dp[e] = max(dp[e - energy] + pleasure, dp[e])

print(dp[100])
