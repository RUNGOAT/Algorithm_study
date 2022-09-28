import sys
input = sys.stdin.readline
from collections import deque


def bfs(v):
    flag = 0
    q = deque([v])
    while q:
        v = q.popleft()
        for w in adj_list[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
                flag = 1
    return flag


N, M = map(int, input().split())
adj_list = [[i] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
visited = [0] * (N+1)
ans = 0
if M == 0:
    ans = N
else:
    for i in range(1, N+1):
        ans += bfs(i)
print(ans)
