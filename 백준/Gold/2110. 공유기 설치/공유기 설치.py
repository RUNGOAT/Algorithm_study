import sys
input = sys.stdin.readline


N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
s = 1
e = arr[-1] - arr[0]
ans = 0
while s <= e:
    mid = (s + e) // 2
    cur = arr[0]
    cnt = 1

    for n in range(1, N):
        if arr[n] - cur >= mid:
            cnt += 1
            cur = arr[n]

    if cnt >= C:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
