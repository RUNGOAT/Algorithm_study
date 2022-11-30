import sys
input = sys.stdin.readline


N = int(input())
perm = list(map(int, input().split()))

if perm == sorted(perm, reverse=True):
    print(-1)
else:
    for i in range(N - 1, 0, -1):
        if perm[i-1] < perm[i]:
            for j in range(N - 1, 0, -1):
                if perm[i-1] < perm[j]:
                    perm[i-1], perm[j] = perm[j], perm[i-1]
                    perm = perm[:i] + sorted(perm[i:])
                    print(' '.join(map(str, perm)))
                    exit(0)
