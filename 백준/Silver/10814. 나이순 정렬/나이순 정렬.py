import sys
input = sys.stdin.readline


N = int(input())
arr = [list(input().split()) for _ in range(N)]
for ans in sorted(arr, key=lambda x: int(x[0])):
    print(' '.join(ans))
