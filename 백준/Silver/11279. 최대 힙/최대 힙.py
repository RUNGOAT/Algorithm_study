import sys, heapq
input = sys.stdin.readline


N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, -x)
    else:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
        