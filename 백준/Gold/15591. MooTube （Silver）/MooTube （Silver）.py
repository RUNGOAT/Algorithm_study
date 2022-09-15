import sys


def bfs(k, v):
    q = [v]
    visited = [0] * (N+1)
    while q:
        v = q.pop(0)
        visited[v] = 1
        for i in range(len(adj_list[v])):
            if visited[adj_list[v][i]] == 0 and usado[v][i] >= k:
                q.append(adj_list[v][i])
                usado_tmp.append(usado[v][i])


N, Q = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
usado = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    adj_list[p].append(q)
    adj_list[q].append(p)
    usado[p].append(r)
    usado[q].append(r)
for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    usado_tmp = []
    bfs(k, v)
    print(len(usado_tmp))
