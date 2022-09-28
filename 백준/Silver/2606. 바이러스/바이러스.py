import sys
input = sys.stdin.readline


def dfs(v):
    global ans
    visited[v] = 1
    ans += 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)


V = int(input())
E = int(input())
adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)
visited = [0] * (V+1)
ans = -1
dfs(1)
print(ans)
