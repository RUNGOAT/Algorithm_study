import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

max_cnt = 0
cnt = 1
for i in range(1, N):
    if sequence[i-1] <= sequence[i]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1
if max_cnt < cnt:
    max_cnt = cnt
    
cnt = 1
for i in range(1, N):
    if sequence[i-1] >= sequence[i]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1
if max_cnt < cnt:
    max_cnt = cnt

print(max_cnt)
