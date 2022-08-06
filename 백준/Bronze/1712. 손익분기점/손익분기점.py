import sys
a, b, c = map(int, sys.stdin.readline().split())

if c > b:
    print((a // (c-b)) + 1)
else:
    print(-1)