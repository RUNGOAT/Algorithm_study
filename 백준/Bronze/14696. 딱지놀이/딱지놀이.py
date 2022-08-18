import sys


def victory():
    for j in range(4, 0, -1):
        if card_a.count(j) > card_b.count(j):
            return 'A'
        elif card_a.count(j) < card_b.count(j):
            return 'B'
    return 'D'


N = int(sys.stdin.readline())
for i in range(1, N + 1):
    a, *card_a = map(int, input().split())
    b, *card_b = map(int, input().split())

    print(victory())
