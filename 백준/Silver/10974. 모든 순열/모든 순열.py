import sys
input = sys.stdin.readline


def perm(n, k):
    if k == n:
        print(' '.join(map(str, p)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            p[k] = i + 1
            perm(n, k+1)
            visited[i] = False


N = int(input())
visited = [False] * N
p = [0] * N
perm(N, 0)