import sys

N = int(sys.stdin.readline())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    s, e, w, h = map(int, sys.stdin.readline().split())
    for i in range(h):
        for j in range(w):
            arr[e+i][s+j] = n

cnt = [0] * (N+1)
for x in range(1001):
    for y in range(1001):
        cnt[arr[x][y]] += 1

for i in range(1, N+1):
    print(cnt[i])