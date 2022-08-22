import sys

N, K = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

total = 0
for j in range(K):
    total += sequence[j]
max_total = total

for i in range(1, N-K+1):
    total -= sequence[i-1]
    total += sequence[i+K-1]
    if max_total < total:
        max_total = total

print(max_total)
