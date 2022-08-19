import sys

arr = [[0] * 101 for _ in range(101)]
N = int(sys.stdin.readline())
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            arr[s+i][e+j] = 1

print(sum(sum(k) for k in arr))
