import sys
input = sys.stdin.readline


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(fx, fy):
    if fx < fy:
        p[fy] = fx
    else:
        p[fx] = fy


N, M = map(int, input().split())
p = list(range(N+1))
edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))
edge.sort(key=lambda x: x[2])
cnt = 0
ans = 0
for u, v, c in edge:
    fu = find_set(u)
    fv = find_set(v)
    if fu != fv:
        union(fu, fv)
        ans += c
        cnt += 1
        if cnt == N-2:
            break
print(ans)
