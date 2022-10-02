def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = f(M) // f(N) // f(M-N)
    print(ans)
    