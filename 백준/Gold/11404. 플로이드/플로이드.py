import heapq
import sys
input = sys.stdin.readline


def dijkstra(v):
    heap = []
    heapq.heappush(heap, (0, v))
    D[v] = 0
    while heap:
        d, v = heapq.heappop(heap)
        for c, w in adjL[v]:
            cost = d + c
            if D[w] > cost:
                D[w] = cost
                heapq.heappush(heap, (cost, w))


INF = int(1e9)
N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adjL[a].append((c, b))

for n in range(1, N+1):
    D = [INF] * (N+1)
    dijkstra(n)
    for i in range(1, N+1):
        if D[i] == INF:
            print(0, end=' ')
        else:
            print(D[i], end=' ')
    print()
