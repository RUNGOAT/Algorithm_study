import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
perm = sorted(list(map(int, input().split())))
for p in permutations(perm, M):
    print(' '.join(map(str, p)))