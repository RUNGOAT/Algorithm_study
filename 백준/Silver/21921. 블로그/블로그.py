import sys
input = sys.stdin.readline


N, X = map(int, input().split())
arr = list(map(int, input().split()))

max_visitor = 0
max_count = 1
for x in range(X):
    max_visitor += arr[x]

ssum = max_visitor
for i in range(N-X):
    visitor = ssum
    visitor -= arr[i]
    visitor += arr[i+X]
    if (max_visitor < visitor):
        max_visitor = visitor
        max_count = 1
    elif max_visitor == visitor:
        max_count += 1
    ssum = visitor

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(max_count)