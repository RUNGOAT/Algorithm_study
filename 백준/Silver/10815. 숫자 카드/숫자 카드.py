import sys


def binary(s, e, t):
    while s <= e:
        mid = (s+e) // 2
        if card_num[mid] == t:
            return 1
        elif card_num[mid] < t:
            s = mid + 1
        else:
            e = mid - 1
    return 0


N = int(sys.stdin.readline())
card_num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_card_num = list(map(int, sys.stdin.readline().split()))

card_num.sort()

result = []
for i in range(M):
    result.append(binary(0, N-1, M_card_num[i]))
print(*result)
