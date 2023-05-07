import sys
input = sys.stdin.readline


arr = list(input().rstrip())
size = len(arr)

a_cnt = 0
for i in range(size):
    if arr[i] == 'a':
        a_cnt += 1

ans = 1000000
for i in range(size):
    b_cnt = 0
    for j in range(i, i + a_cnt):
        if arr[j % size] == 'b':
            b_cnt += 1
    ans = min(ans, b_cnt)

print(ans)
