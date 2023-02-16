import sys
input = sys.stdin.readline


N, L = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 1
min_range = arr[0] - 0.5 + L
for i in range(1, N):
    if min_range < arr[i]:
        cnt += 1
        min_range = arr[i] - 0.5 + L
print(cnt)
