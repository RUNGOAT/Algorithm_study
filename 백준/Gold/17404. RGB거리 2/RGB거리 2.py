import sys
input = sys.stdin.readline


def f(x):
    dp = [[INF, INF, INF] for _ in range(N)]
    for i in range(3):
        if i != x:
            dp[1][i] = arr[1][i] + arr[0][x]
    for n in range(2, N):
        dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + arr[n][0]
        dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + arr[n][1]
        dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + arr[n][2]
    return min(dp[N-1][x-1], dp[N-1][x-2])


INF = 1000001
N = int(input())
arr = [[] for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, input().split()))

ans = INF
for k in range(3):
    ans = min(ans, f(k))
print(ans)


