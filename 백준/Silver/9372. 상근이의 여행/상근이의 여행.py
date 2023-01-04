import sys
input = sys.stdin.readline


def bfs(v):
    visited = [False] * (N+1)
    stack = [v]
    visited[v] = True
    cnt = 0
    while stack:
        v = stack.pop()
        for w in adjL[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)
                cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    tree = list(range(N+1))
    adjL = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjL[a].append(b)
        adjL[b].append(a)
    print(bfs(1))
    