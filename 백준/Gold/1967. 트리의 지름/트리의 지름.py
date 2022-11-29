import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(v, dist):
    global max_dist, far_node
    if max_dist < dist:
        max_dist = dist
        far_node = v

    visited[v] = True
    for w, d in adjL[v]:
        if not visited[w]:
            dfs(w, dist + d)


N = int(input())
E = N - 1
adjL = [[] for _ in range(N+1)]
for n in range(E):
    v, w, d = map(int, input().split())
    adjL[v].append([w, d])
    adjL[w].append([v, d])

max_dist = 0
far_node = 0
visited = [False] * (N+1)
dfs(1, 0)
visited = [False] * (N+1)
dfs(far_node, 0)
print(max_dist)
