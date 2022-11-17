import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    arr.add(input().strip())
arr = list(arr)
arr.sort(key=lambda x: (len(x), x))

for i in range(len(arr)):
    print(arr[i])
