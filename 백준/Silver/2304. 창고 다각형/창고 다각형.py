import sys

N = int(sys.stdin.readline())

storage = [0] * 1001
max_l = 0
for _ in range(N):
    l, h = map(int, sys.stdin.readline().split())
    storage[l] = h

area = 0
max_h_idx = storage.index(max(storage))

height = 0
for i in range(max_h_idx):
    if height < storage[i]:
        height = storage[i]
    area += height

area += storage[max_h_idx]

height = 0
for i in range(1000, max_h_idx, -1):
    if height < storage[i]:
        height = storage[i]
    area += height

print(area)
