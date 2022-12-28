import sys
input = sys.stdin.readline


N = input().rstrip()
print(''.join(sorted(N, reverse=True)))
