import sys
input = sys.stdin.readline


def solution():
    N, kim, lim = map(int, input().split())
    round = 0
    while N != 1:
        if not (kim == N and N % 2):
            kim = (kim % 2) + kim // 2
        else:
            kim = kim // 2 + 1
        if not (lim == N and N % 2):
            lim = (lim % 2) + lim // 2
        else:
            lim = lim // 2 + 1
        N = (N % 2) + N // 2
        round += 1
        if kim == lim:
            return round
    return -1

print(solution())
