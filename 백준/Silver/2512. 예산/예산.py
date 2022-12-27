import sys
input = sys.stdin.readline


N = int(input())
budget_requests = list(map(int, input().split()))
M = int(input())

s, e = 1, max(budget_requests)

while s <= e:
    mid = (s+e) // 2

    total = 0
    for budget in budget_requests:
        if budget > mid:
            budget = mid
        total += budget

    if total <= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)
