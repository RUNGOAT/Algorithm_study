import sys
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
for x, y in sorted(arr, key=lambda x: (x[0], x[1])):
    print(x, y)