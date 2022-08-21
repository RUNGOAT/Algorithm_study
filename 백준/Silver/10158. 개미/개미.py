import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

i = p
w_list = [p]
d = 1
for _ in range(1, w * 2):
    i += d
    w_list.append(i)
    if i + d == w + 1:
        d = -1
    elif i + d == -1:
        d = 1

j = q
h_list = [q]
d = 1
for _ in range(1, h * 2):
    j += d
    h_list.append(j)
    if j + d == h + 1:
        d = -1
    elif j + d == -1:
        d = 1

print(w_list[t % (w * 2)], h_list[t % (h * 2)])
