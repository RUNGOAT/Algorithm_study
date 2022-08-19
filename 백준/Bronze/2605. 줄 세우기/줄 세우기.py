import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(N):
    result.insert(nums[i], i+1)
print(*result[::-1])
