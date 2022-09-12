import sys

N, M = map(int, sys.stdin.readline().split())
tmp = {}
lst = []
for _ in range(N):
    name = sys.stdin.readline().strip()
    tmp[name] = True
for _ in range(M):
    name = sys.stdin.readline().strip()
    if tmp.get(name):
        lst.append(name)

print(len(lst))
print(*sorted(lst), sep="\n")
