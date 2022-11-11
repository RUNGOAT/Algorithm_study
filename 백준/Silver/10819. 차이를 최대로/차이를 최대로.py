from itertools import permutations
import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

max_ans = 0
for arr in permutations(arr, N):
    ssum = 0
    for i in range(1, N):
        ssum += abs(arr[i-1] - arr[i])
    if max_ans < ssum:
        max_ans = ssum
print(max_ans)