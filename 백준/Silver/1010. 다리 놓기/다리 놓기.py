import sys
input = sys.stdin.readline

def f2(n):
    if len(F) - 1 < n:
        F.append(n * f2(n-1))
    return F[n]

F = [1, 1]
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = f2(M) // f2(N) // f2(M-N)
    print(ans)
