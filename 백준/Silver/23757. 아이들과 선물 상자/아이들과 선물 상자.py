import sys, heapq
input = sys.stdin.readline


def solution():
    for child in children:
        gift = heapq.heappop(gifts) * -1
        diff = gift - child
        if diff >= 0:
            heapq.heappush(gifts, -diff)
        else:
            return 0
    return 1


N, M = map(int, input().split())
gifts = list(map(lambda x: int(x) * -1, input().split()))
children = list(map(int, input().split()))
heapq.heapify(gifts)
print(solution())
