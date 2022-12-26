import sys
input = sys.stdin.readline


K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
s, e = 1, max(lan)

while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for k in lan:
        cnt += k // mid

    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1
print(e)
