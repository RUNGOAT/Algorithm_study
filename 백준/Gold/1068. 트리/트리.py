import sys


def dfs(v):
    global cnt
    visited[v] = 1

    if adj_list[v]:
        for w in adj_list[v]:
            if visited[w] == 0:
                dfs(w)
    else:
        if v != delete_node:
            cnt += 1


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
for i in range(N):
    if arr[i] == -1:
        root = i
    if i == delete_node or arr[i] == delete_node or arr[i] == -1:
        continue
    adj_list[arr[i]].append(i)

visited = [0] * N
cnt = 0
dfs(root)

print(cnt)
