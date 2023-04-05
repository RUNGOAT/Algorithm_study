from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N
if N == 1:
    print(0)
    exit(0)

def bfs():
    global ans
    q = deque()
    q.append(0)
    while q:
        a = q.popleft()
        for i in range(a+1, a+1+arr[a]):
            if i >= N:      continue
            if visited[i]:  continue
            visited[i] = visited[a] + 1
            q.append(i)


bfs()
print(visited[-1] if visited[-1] else -1)
