import sys
sys.setrecursionlimit(10**5)


def dfs(v):
    global cnt
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            cnt += 1
            dfs(w)
            cnt -= 1
        else:
            if len(adj_list[v]) == 1:
                cnt_list.append(cnt)


V = int(sys.stdin.readline())
E = V-1
adj_list = [[] for _ in range(V+1)]
visited = [0] * (V + 1)

for i in range(E):
    a, b = list(map(int, sys.stdin.readline().split()))
    adj_list[a].append(b)
    adj_list[b].append(a)

cnt = 0
cnt_list = []
dfs(1)
if sum(cnt_list) % 2:
    print('Yes')
else:
    print('No')
