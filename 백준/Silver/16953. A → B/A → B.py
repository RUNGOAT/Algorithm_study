import sys
input = sys.stdin.readline


def dfs(a, b, cnt):
    global ans
    if a > b:
        return
    if a == b:
        ans = cnt + 1
        return
    dfs(a * 2, b, cnt + 1)
    dfs(a * 10 + 1, b, cnt + 1)


A, B = map(int, input().split())
ans = -1
dfs(A, B, 0)
print(ans)
