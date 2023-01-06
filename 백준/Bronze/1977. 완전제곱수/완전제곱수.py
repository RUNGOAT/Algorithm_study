import sys
input = sys.stdin.readline


M = int(input())
N = int(input())

num = 1
ans = []
while num ** 2 <= N:
    if num ** 2 >= M:
        ans.append(num ** 2)
    num += 1

if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)
