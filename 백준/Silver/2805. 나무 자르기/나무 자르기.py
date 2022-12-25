import sys
input = sys.stdin.readline


N, M = map(int, input().split())
tree = list(map(int, input().split()))
s, e = 1, max(tree)

while s <= e:
    mid = (s + e) // 2

    total = 0
    for t in tree:
        if t >= mid:
            total += t - mid

    if total >= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)
