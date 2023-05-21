import sys
input = sys.stdin.readline


H, W = map(int, input().split())
arr = list(map(int, input().split()))

max_height = 0
max_list = []
for i in range(W):
    if max_height == arr[i]:
        max_list.append(i)
    elif max_height < arr[i]:
        max_height = arr[i]
        max_list = [i]

ans = 0
left = 0
tmp = 0
for i in range(max_list[0] + 1):
    if arr[i] < left:
        tmp += left - arr[i]
    else:
        left = arr[i]
        ans += tmp
        tmp = 0

right = 0
tmp = 0
for i in range(W-1, max_list[len(max_list) - 1] - 1, -1):
    if arr[i] < right:
        tmp += right - arr[i]
    else:
        right = arr[i]
        ans += tmp
        tmp = 0

for i in range(len(max_list) - 1):
    for j in range(max_list[i], max_list[i+1]):
        ans += max_height - arr[j]

print(ans)