import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

w_idx = t % (w * 2)     # w * 2 한 값이 원 위치로 돌아오는 주기
d = 1
for _ in range(1, w_idx+1):
    p += d
    if p + d == w + 1:
        d = -1
    elif p + d == -1:
        d = 1

h_idx = t % (h * 2)     # h * 2 한 값이 원 위치로 돌아오는 주기
d = 1
for _ in range(1, h_idx+1):
    q += d
    if q + d == h + 1:
        d = -1
    elif q + d == -1:
        d = 1

print(p, q)
