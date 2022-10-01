import heapq
import sys
input = sys.stdin.readline


def dijkstra(s):
    D[s] = 0
    heap = []
    heapq.heappush(heap, (D[s], s))
    while heap:
        d, u = heapq.heappop(heap)
        for v in adj[u]:
            if D[v[0]] > D[u] + v[1]:
                D[v[0]] = D[u] + v[1]
                heapq.heappush(heap, (D[v[0]], v[0]))


INF = 99999999
V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
D = [INF] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])
dijkstra(K)
for i in range(1, V+1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])
