import heapq
import sys
input = sys.stdin.readline


def dijkstra(s, e):
    D[s] = 0
    heap = [[D[s], s]]
    while heap:
        w, u = heapq.heappop(heap)
        if w > D[u]:
            continue
        for v, w in adjL[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                heapq.heappush(heap, [D[v], v])


INF = int(1e9)
N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adjL[u].append([v, w])
s, e = map(int, input().split())
D = [INF] * (N+1)
dijkstra(s, e)
print(D[e])
