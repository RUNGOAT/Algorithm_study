import sys

width, height = map(int, sys.stdin.readline().split())
w_list = [0, width]
h_list = [0, height]
K = int(sys.stdin.readline())
for _ in range(K):
    direction, num = map(int, sys.stdin.readline().split())
    if direction == 0:
        h_list.append(num)
    else:
        w_list.append(num)

w_list.sort()
h_list.sort()

max_w = 0
for i in range(1, len(w_list)):
    if max_w < w_list[i] - w_list[i-1]:
        max_w = w_list[i] - w_list[i-1]
max_h = 0
for i in range(1, len(h_list)):
    if max_h < h_list[i] - h_list[i-1]:
        max_h = h_list[i] - h_list[i-1]

print(max_w * max_h)
