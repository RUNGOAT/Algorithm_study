import sys
input = sys.stdin.readline


arr = set()
for _ in range(10):
    a = int(input())
    arr.add(a % 42)
print(len(arr))
