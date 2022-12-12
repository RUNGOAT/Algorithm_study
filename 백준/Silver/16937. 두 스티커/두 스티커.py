import sys
input = sys.stdin.readline


H, W = map(int, input().split())
N = int(input())
arr = []
for _ in range(N):
    r, c = map(int, input().split())
    arr.append((r, c))
max_area = 0
for i in range(N):
    r1, c1 = arr[i]
    for j in range(i+1, N):
        r2, c2 = arr[j]
        if (r1 + r2 <= H and max(c1, c2) <= W) or (max(r1, r2) <= H and c1 + c2 <= W):
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if (c1 + r2 <= H and max(r1, c2) <= W) or (max(c1, r2) <= H and r1 + c2 <= W):
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if (c1 + c2 <= H and max(r1, r2) <= W) or (max(c1, c2) <= H and r1 + r2 <= W):
            max_area = max(max_area, r1 * c1 + r2 * c2)
        if (r1 + c2 <= H and max(c1, r2) <= W) or (max(r1, c2) <= H and c1 + r2 <= W):
            max_area = max(max_area, r1 * c1 + r2 * c2)

print(max_area)
