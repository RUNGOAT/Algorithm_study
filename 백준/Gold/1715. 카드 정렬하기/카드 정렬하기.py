import sys, heapq
input = sys.stdin.readline


N = int(input())
heap = [int(input()) for _ in range(N)]
heapq.heapify(heap)
ans = 0
while len(heap) != 1:
    compare = heapq.heappop(heap) + heapq.heappop(heap)
    ans += compare
    heapq.heappush(heap, compare)
print(ans)
