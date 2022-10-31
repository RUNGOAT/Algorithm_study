import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ssum = [-1000] * N
delete_one_sum = [-1000] * N

ssum[0] = delete_one_sum[0] = arr[0]
for i in range(1, N):
    ssum[i] = max(ssum[i-1] + arr[i], arr[i])
    delete_one_sum[i] = max(delete_one_sum[i-1] + arr[i], ssum[i-1])

print(max(max(ssum), max(delete_one_sum)))