from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 0))
    while q:
        s, c = q.popleft()
        if s == S:
            return visited[s][c]
        if s != 0 and not visited[s][s]:
            visited[s][s] = visited[s][c] + 1
            q.append((s, s))
        if s+c <= S and not visited[s+c][c]:
            visited[s+c][c] = visited[s][c] + 1
            q.append((s+c, c))
        if s > 0 and not visited[s-1][c]:
            visited[s-1][c] = visited[s][c] + 1
            q.append((s-1, c))


S = int(input())
visited = [[0] * (S) for _ in range(2*S)]
print(bfs())
