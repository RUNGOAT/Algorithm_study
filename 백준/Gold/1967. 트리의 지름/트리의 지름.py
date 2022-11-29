import sys
input = sys.stdin.readline


def bfs(v):
    global max_dist
    far_node = 0
    stack = [[v, 0]]
    visited = [False] * (N + 1)
    visited[v] = True
    while stack:
        v, d = stack.pop()
        if max_dist < d:
            max_dist = d
            far_node = v
        for w, dist in adjL[v]:
            if not visited[w]:
                visited[w] = True
                stack.append([w, d + dist])

    return far_node


N = int(input())
E = N - 1
adjL = [[] for _ in range(N+1)]
for n in range(E):
    v, w, d = map(int, input().split())
    adjL[v].append([w, d])
    adjL[w].append([v, d])

max_dist = 0
node = bfs(1)
bfs(node)
print(max_dist)
