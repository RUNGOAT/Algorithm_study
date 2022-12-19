import sys
input = sys.stdin.readline


def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])   # 경로 압축
    return p[x]


def union(fu, fv):
    if fu > fv:
        p[fu] = fv
    else:
        p[fv] = fu


V, E = map(int, input().split())
edge = []
p = list(range(V+1))

for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, u, v])
edge.sort(key=lambda x: x[0])

total = 0
for w, u, v in edge:
    fu = find_set(u)
    fv = find_set(v)
    if fu != fv:
        union(fu, fv)
        total += w

print(total)
