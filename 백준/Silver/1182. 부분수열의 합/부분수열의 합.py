import sys
input = sys.stdin.readline


def powerset(n, k, s):
    global ans
    if k == n:
        if s == S:
            ans += 1
    else:
        powerset(n, k + 1, s + arr[k])
        powerset(n, k + 1, s)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
if S == 0:
    ans -= 1
powerset(N, 0, 0)
print(ans)
