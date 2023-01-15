import sys, heapq
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    for n in range(N-2):
        ans = max(ans, abs(arr[n] - arr[n+2]))
    print(ans)
