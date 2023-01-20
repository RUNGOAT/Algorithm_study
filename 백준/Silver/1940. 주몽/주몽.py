import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
s, e = 0, N-1
while s < e:
    ssum = arr[s] + arr[e]
    if ssum < M:
        s += 1
        continue
    elif ssum == M:
        ans += 1
    e -= 1
print(ans)