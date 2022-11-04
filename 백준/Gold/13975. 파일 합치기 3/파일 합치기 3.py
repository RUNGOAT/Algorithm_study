from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    heap = sorted(list(map(int, input().split())))
    ans = 0
    while len(heap) != 1:
        C1 = heappop(heap)
        C2 = heappop(heap)
        ans += C1 + C2
        heappush(heap, C1 + C2)
    print(ans)