import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
if n > 1:
    nums[1][0] += nums[0][0]
    nums[1][1] += nums[0][0]
    for i in range(2, n):
        nums[i][0] += nums[i-1][0]
        for j in range(1, i):
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])
        nums[i][-1] += nums[i-1][-1]
print(max(nums[-1]))
