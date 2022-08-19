import sys

N = int(sys.stdin.readline())
arr = [[0] * 1001 for _ in range(1001)]
ans = [0] * (N+1)
for n in range(1, N+1):
    s, e, w, h = map(int, sys.stdin.readline().split())
    for i in range(h):
        for j in range(w):
            if arr[e+i][s+j] != 0:
                ans[arr[e+i][s+j]] -= 1
                arr[e+i][s+j] = n
                ans[arr[e+i][s+j]] += 1
            else:
                arr[e + i][s + j] = n
                ans[arr[e + i][s + j]] += 1

for i in range(1, N+1):
    print(ans[i])