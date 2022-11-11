import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()

ans = 1
heap = [arr[0][1]]
for i in range(1, N):
    if heap[0] <= arr[i][0]:
        heapq.heappop(heap)
    else:
        ans += 1
    heapq.heappush(heap, arr[i][1])
print(ans)
