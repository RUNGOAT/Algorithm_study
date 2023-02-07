import sys
input = sys.stdin.readline


def solution():
    N, score, P = map(int, input().split())
    if N:
        ranking_list = list(map(int, input().split()))
    else:
        return 1
    num = 0
    for rank in range(N):
        if ranking_list[rank] < score:
            if num:
                return num
            return rank + 1
        elif ranking_list[rank] == score:
            if num == 0:
                num = rank + 1
    if N < P:
        if num:
            return num
        return N + 1
    else:
        return -1


print(solution())