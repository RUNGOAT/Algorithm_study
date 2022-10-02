F = [1] * 31
for i in range(2, 31):
    F[i] = F[i-1] * i

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = F[M] // F[N] // F[M-N]
    print(ans)
