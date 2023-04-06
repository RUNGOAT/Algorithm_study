import sys
input = sys.stdin.readline


def check(lst, start):
    global ans
    for i in range(start, len(lst), M):
        ans += abs(lst[i]) * 2


N, M = map(int, input().split())
arr = list(map(int, input().split()))
negative = []
positive = []

for i in range(N):
    if arr[i] > 0:
        positive.append(arr[i])
    else:
        negative.append(arr[i])

positive.sort(reverse=True)
negative.sort()

ans = 0
if not positive:
    ans += abs(negative[0])
    check(negative, M)
elif not negative:
    ans += positive[0]
    check(positive, M)
elif positive[0] > abs(negative[0]):
    ans += positive[0]
    check(positive, M)
    check(negative, 0)
else:
    ans += abs(negative[0])
    check(negative, M)
    check(positive, 0)

print(ans)
