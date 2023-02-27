import sys
input = sys.stdin.readline


N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

ans = 0
for n in range(N-1, -1, -1):
    if K >= coin[n]:
        ans += K // coin[n]
        K %= coin[n]
print(ans)
