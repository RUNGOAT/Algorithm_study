from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        sx, sy = q.popleft()
        if abs(ex - sx) + abs(ey - sy) <= 1000:
            return 'happy'
        for i in range(N):
            if not visited[i]:
                x, y = market[i]
                if abs(x - sx) + abs(y - sy) <= 1000:
                    q.append([x, y])
                    visited[i] = True
    return 'sad'


T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    market = []
    for n in range(N):
        market.append(list(map(int, input().split())))
    market.sort(key=lambda x: (x[0], x[1]))
    ex, ey = map(int, input().split())
    visited = [False] * N
    print(bfs(sx, sy))
