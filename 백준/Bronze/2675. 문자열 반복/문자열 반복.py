import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    R, S = input().split()
    r = int(R)
    for s in S:
        print(s * r, end='')
    print()
        