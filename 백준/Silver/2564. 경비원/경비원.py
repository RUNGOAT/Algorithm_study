import sys

width, height = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
shop = [[] for _ in range(5)]
for n in range(N):
    direction, length = map(int, sys.stdin.readline().split())
    shop[direction].append(length)

direction_x, length_x = map(int, sys.stdin.readline().split())

if direction_x == 1:    # 북쪽
    total = 0
    for i in range(1, 5):
        if i == 1:
            for num in shop[i]:
                total += abs(length_x - num)
        elif i == 2:
            for num in shop[i]:
                temp = length_x + num + height
                total += min(temp, 2 * (width + height) - temp)
        elif i == 3:
            for num in shop[i]:
                total += length_x + num
        elif i == 4:
            for num in shop[i]:
                total += width - length_x + num

elif direction_x == 2:    # 남쪽
    total = 0
    for i in range(1, 5):
        if i == 1:
            for num in shop[i]:
                temp = length_x + num + height
                total += min(temp, 2 * (width + height) - temp)
        elif i == 2:
            for num in shop[i]:
                total += abs(length_x - num)
        elif i == 3:
            for num in shop[i]:
                total += length_x + height - num
        elif i == 4:
            for num in shop[i]:
                total += width - length_x + height - num

elif direction_x == 3:    # 서쪽
    total = 0
    for i in range(1, 5):
        if i == 1:
            for num in shop[i]:
                total += length_x + num
        elif i == 2:
            for num in shop[i]:
                total += height - length_x + num
        elif i == 3:
            for num in shop[i]:
                total += abs(length_x - num)
        elif i == 4:
            for num in shop[i]:
                temp = length_x + num + width
                total += min(temp, 2 * (width + height) - temp)

elif direction_x == 4:    # 동쪽
    total = 0
    for i in range(1, 5):
        if i == 1:
            for num in shop[i]:
                total += length_x + width - num
        elif i == 2:
            for num in shop[i]:
                total += height - length_x + width - num
        elif i == 3:
            for num in shop[i]:
                temp = length_x + num + width
                total += min(temp, 2 * (width + height) - temp)
        elif i == 4:
            for num in shop[i]:
                total += abs(length_x - num)

print(total)
