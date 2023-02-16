import sys
input = sys.stdin.readline


N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
max_tmp = [0, 0, 0]
min_tmp = [0, 0, 0]
for n in range(N):
    arr = list(map(int, input().split()))
    for j in range(3):
        if j == 0:
            max_tmp[j] = max(max_dp[j], max_dp[j + 1]) + arr[0]
            min_tmp[j] = min(min_dp[j], min_dp[j + 1]) + arr[0]
        elif j == 1:
            max_tmp[j] = max(max_dp[j - 1], max_dp[j], max_dp[j + 1]) + arr[1]
            min_tmp[j] = min(min_dp[j - 1], min_dp[j], min_dp[j + 1]) + arr[1]
        else:
            max_tmp[j] = max(max_dp[j - 1], max_dp[j]) + arr[2]
            min_tmp[j] = min(min_dp[j - 1], min_dp[j]) + arr[2]
    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))
