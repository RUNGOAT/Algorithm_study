import sys


def empty_area():
    '''
    문제에서 반시계 방향 고정
    empty_area_sequence : 빈 면적에 해당하는 방향값 순서를 담은 배열
    연속된 두 개의 숫자가 입력 배열(direction)에 있을 때의 길이가 빈 면적의 가로, 세로 길이
    '''
    empty_area_sequence = [1, 3, 2, 4, 1]
    for i in range(4):          # empty_area_sequence 배열 길이 - 1
        for j in range(5):      # direction 배열 길이 - 1
            if [empty_area_sequence[i], empty_area_sequence[i + 1]] == [direction[j], direction[j + 1]]:
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

print(K * (area - empty_area()))
