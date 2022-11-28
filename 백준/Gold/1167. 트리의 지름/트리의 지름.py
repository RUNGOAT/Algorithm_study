import sys, heapq
input = sys.stdin.readline


def dfs(v, d):
    global max_d, far_node
    if max_d < d:
        max_d = d
        far_node = v

    visited[v] = True
    for w, dist in adjL[v]:
        if not visited[w]:
            dfs(w, d + dist)


V = int(input())
ans = 0
adjL = [[] for _ in range(V+1)]
for i in range(V):
    tmp = list(map(int, input().split()))

    j = 1
    while tmp[j] != -1:
        adjL[tmp[0]].append([tmp[j], tmp[j+1]])
        j += 2

max_d = 0
far_node = 0
visited = [False] * (V+1)
dfs(1, 0)
visited = [False] * (V + 1)
dfs(far_node, 0)
print(max_d)
