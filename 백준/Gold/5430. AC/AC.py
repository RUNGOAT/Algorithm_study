import sys
from collections import deque


def f(p):
    cnt_R = 0
    for i in range(len(p)):
        if p[i] == 'R':
            cnt_R += 1
        else:
            if not queue:
                return 'error'
            if cnt_R % 2:
                queue.pop()
            else:
                queue.popleft()
    if cnt_R % 2:
        queue.reverse()

    return f"[{','.join(map(str, queue))}]"


T = int(sys.stdin.readline())
for _ in range(T):
    P = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    tmp = sys.stdin.readline()
    if n == 0:
        queue = deque([])
    else:
        queue = deque(map(int, tmp.strip('[\n]').split(',')))

    print(f(P))
