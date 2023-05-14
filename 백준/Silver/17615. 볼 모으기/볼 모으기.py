import sys
input = sys.stdin.readline


def check(target, start, end, dir):
    res = cnt = 0
    i = start if dir == 'LEFT' else end - 1
    limit = end if dir == 'LEFT' else start
    step = 1 if dir == 'LEFT' else -1

    while (i < limit) if dir == 'LEFT' else (i >= limit):
        if line[i] != target:
            cnt = 1
        else:
            res += cnt
        i += step

    return res


N = int(input())
line = list(input().rstrip())

ans = 500001
ans = min(check('R', 0, N, 'LEFT'),
          check('B', 0, N, 'LEFT'),
          check('R', 0, N, 'RIGHT'),
          check('B', 0, N, 'RIGHT'),
          ans)
print(ans)