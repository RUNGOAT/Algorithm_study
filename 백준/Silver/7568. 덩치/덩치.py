import sys

N = int(sys.stdin.readline())
bulk = []
for n in range(N):
    w, h = map(int, sys.stdin.readline().split())
    bulk.append((w, h))

for weight, height in bulk:
    rank = 0
    for w, h in bulk:
        if weight < w and height < h:
            rank += 1
    print(rank+1, end=' ')
    