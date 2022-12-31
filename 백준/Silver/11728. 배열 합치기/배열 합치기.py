import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.extend(list(map(int, input().split())))
print(' '.join(map(str, sorted(arr))))
