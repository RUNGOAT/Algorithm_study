import heapq
import sys
input = sys.stdin.readline


def dijkstra(v):
    heap = []
    heapq.heappush(heap, (0, v))
    D[v] = 0
    while heap:
        d, v = heapq.heappop(heap)
        for w in range(1, N+1):
            cost = d + adjM[v][w]
            if D[w] > cost:
                D[w] = cost
                heapq.heappush(heap, (cost, w))


INF = 100000000
N = int(input())
M = int(input())
adjM = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adjM[a][b] = min(adjM[a][b], c)

for n in range(1, N+1):
    D = [INF] * (N+1)
    dijkstra(n)
    for i in range(1, N+1):
        if D[i] == INF:
            print(0, end=' ')
        else:
            print(D[i], end=' ')
    print()
