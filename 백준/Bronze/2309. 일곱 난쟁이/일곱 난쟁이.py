import sys
from itertools import combinations

N = []
for i in range(9):
    N += [int(sys.stdin.readline())]

temp = list(combinations(N, 7))
for dwarf in temp:
    if sum(dwarf) == 100:
        dwarf = sorted(list(dwarf))
        print(*dwarf, sep='\n')
        break
