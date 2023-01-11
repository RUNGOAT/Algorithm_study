import sys
input = sys.stdin.readline


N = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
s, e = 0, N-1
ans = 0
while s < e:
    ssum = arr[s] + arr[e]
    if ssum < x:
        s += 1
    elif ssum > x:
        e -= 1
    else:
        ans += 1
        e -= 1
print(ans)
