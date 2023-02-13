import sys
input = sys.stdin.readline


def dfs(s, b, n, cnt):
    global ans
    if cnt != 0:
        ans = min(ans, abs(s - b))
    if n == N:
        return
    ss, bb = arr[n]
    dfs(s * ss, b + bb, n+1, cnt + 1)
    dfs(s, b, n+1, cnt)


N = int(input())
arr = []
for _ in range(N):
    S, B = map(int, input().split())
    arr.append((S, B))
ans = 1000000000
dfs(1, 0, 0, 0)
print(ans)
