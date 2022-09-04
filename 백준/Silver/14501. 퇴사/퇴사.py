import sys

N = int(sys.stdin.readline())
dp = [0] * 21
T = [0]
P = [0]
for n in range(1, N+1):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(N, 0, -1):
    if i + T[i] <= N+1:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[1])
