import sys
input = sys.stdin.readline


N = input().rstrip()
print(*sorted(N, reverse=True), sep='')
