import sys
input = sys.stdin.readline

N = int(input())
rope = []
for _ in range(N):
    w = int(input())
    rope.append(w)
ans = 0
rope.sort(reverse=True)
for i in range(N):
    ans = max(ans, (i+1) * rope[i])
print(ans)