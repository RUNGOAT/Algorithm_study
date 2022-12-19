import sys
input = sys.stdin.readline


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(fu, fv):
    if fu > fv:
        p[fu] = fv
    else:
        p[fv] = fu


INF = 1000000
V, E = map(int, input().split())
edge = []
p = [i for i in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, u, v])
edge.sort()

cnt = 0
total = 0
for w, u, v in edge:
    fu = find_set(u)
    fv = find_set(v)
    if fu != fv:
        cnt += 1
        union(fu, fv)
        total += w
        if cnt == V:
            break
print(total)
