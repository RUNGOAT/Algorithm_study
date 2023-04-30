import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * 100001
s = e = 0
ans = 0
while s < N:
    while e < N and cnt[arr[e]] < K:
        cnt[arr[e]] += 1
        e += 1

    size = e - s
    ans = max(ans, size)
    cnt[arr[s]] -= 1
    s += 1
print(ans)