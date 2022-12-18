import sys
input = sys.stdin.readline


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    fx = find_set(x)
    fy = find_set(y)
    if fx == fy:
        return True
    if fx < fy:
        p[fy] = fx
    else:
        p[fx] = fy
    return False


N, M = map(int, input().split())
p = [i for i in range(N)]
for m in range(M):
    x, y = map(int, input().split())
    if union(x, y):
        print(m+1)
        exit(0)
print(0)
