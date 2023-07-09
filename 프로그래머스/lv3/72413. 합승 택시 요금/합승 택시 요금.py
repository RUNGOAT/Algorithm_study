import heapq


def dijkstra(start, dist):
    global graph
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, idx = heapq.heappop(q)
        if dist[idx] < cost:
            continue
        for next_cost, next_idx in graph[idx]:
            if dist[next_idx] > cost + next_cost:
                dist[next_idx] = cost + next_cost
                heapq.heappush(q, (dist[next_idx], next_idx))
    return dist


def solution(n, s, a, b, fares):
    global graph
    answer = float('inf')
    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        graph[fare[0]].append((fare[2], fare[1]))
        graph[fare[1]].append((fare[2], fare[0]))

    distA = [float('inf')] * (n + 1)
    distB = [float('inf')] * (n + 1)
    dist = [float('inf')] * (n + 1)

    distA = dijkstra(a, distA)
    distB = dijkstra(b, distB)
    dist = dijkstra(s, dist)

    for i in range(1, n + 1):
        answer = min(answer, distA[i] + distB[i] + dist[i])

    return answer

