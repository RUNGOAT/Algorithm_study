import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

w_idx = t % (w * 2)
h_idx = t % (h * 2)

i = p
w_list = [p]
d = 1
for _ in range(1, w_idx+1):
    i += d
    w_list.append(i)
    if i + d == w + 1:
        d = -1
    elif i + d == -1:
        d = 1

j = q
h_list = [q]
d = 1
for _ in range(1, h_idx+1):
    j += d
    h_list.append(j)
    if j + d == h + 1:
        d = -1
    elif j + d == -1:
        d = 1

print(w_list[-1], h_list[-1])
