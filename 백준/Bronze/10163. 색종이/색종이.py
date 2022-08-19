import sys

N = int(sys.stdin.readline())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    s, e, w, h = map(int, sys.stdin.readline().split())
    for i in range(h):
        for j in range(w):
            arr[e+i][s+j] = n

for x in range(1, N+1):
    cnt = 0
    for y in range(1001):
        cnt += arr[y].count(x)
    print(cnt)
