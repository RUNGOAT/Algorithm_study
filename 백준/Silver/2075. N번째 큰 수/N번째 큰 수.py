import sys, heapq
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
heap = arr
heapq.heapify(heap)
for i in range(1, N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[j])
print(heap[0])

