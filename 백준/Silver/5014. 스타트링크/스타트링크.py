from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(S)
    visited = [0] * 1000001
    visited[S] = 1
    while q:
        s = q.popleft()
        if s == G:
            return visited[s] - 1
        ns = s + U
        if ns <= F and visited[ns] == 0:
            q.append(ns)
            visited[ns] = visited[s] + 1
        ns = s - D
        if ns > 0 and visited[ns] == 0:
            q.append(ns)
            visited[ns] = visited[s] + 1

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())
print(bfs())
