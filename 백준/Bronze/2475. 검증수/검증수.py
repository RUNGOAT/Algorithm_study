import sys
input = sys.stdin.readline


arr = list(map(lambda x: int(x) ** 2, input().split()))
print(sum(arr) % 10)