import sys, heapq
input = sys.stdin.readline


N, K = map(int, input().split())

jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
heapq.heapify(jewels)
bags.sort()

ans = 0
high_value_heap = []
for weight in bags:
    while jewels and weight >= jewels[0][0]:
        heapq.heappush(high_value_heap, -heapq.heappop(jewels)[1])
    if high_value_heap:
        ans += -heapq.heappop(high_value_heap)
print(ans)
