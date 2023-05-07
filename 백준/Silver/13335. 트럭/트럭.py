from collections import deque
import sys
input = sys.stdin.readline


n, w, L = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
time = 0
crossed = 0
idx = 0
ssum = 0

while crossed < n:
    time += 1
    if q and time - q[0][1] == w:
        ssum -= q.popleft()[0]
        crossed += 1

    if idx < n and ssum + arr[idx] <= L:
        q.append((arr[idx], time))
        ssum += arr[idx]
        idx += 1

print(time)
