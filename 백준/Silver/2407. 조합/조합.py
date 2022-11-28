import sys
input = sys.stdin.readline


def f(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


n, m = map(int, input().split())
print(f(n) // (f(n-m) * f(m)))
