import sys
input = sys.stdin.readline


def check(players, l, n):
    if len(players) == M:
        return False
    if players and abs(players[0][0] - l) > 10:
        return False
    return True


P, M = map(int, input().split())
lst = [[]]

for _ in range(P):
    l, n = input().split()
    l = int(l)

    is_entered = False
    for players in lst:
        if check(players, l, n):
            players.append((l, n))
            is_entered = True
            break
    if not is_entered:
        lst.append([(l, n)])

for players in lst:
    if len(players) == M:
        print("Started!")
    else:
        print("Waiting!")
    for l, n in sorted(players, key=lambda x: x[1]):
        print(l, n)
