import sys


def empty_area_check():
    for i in range(4):
        for j in range(5):
            if [empty_area[i], empty_area[i + 1]] == [direction[j], direction[j + 1]]:
                return length[j] * length[j + 1]
    return length[0] * length[-1]


K = int(sys.stdin.readline())
width = []
height = []
direction = []
length = []
for _ in range(6):
    d, l = map(int, sys.stdin.readline().split())
    direction.append(d)
    length.append(l)
    if d == 1 or d == 2:
        width.append(l)
    else:
        height.append(l)

area = max(width) * max(height)
empty_area = [1, 3, 2, 4, 1]

print(K * (area - empty_area_check()))
