import sys

N, K = map(int, sys.stdin.readline().split())

male = {}
female = {}
for _ in range(N):
    s, y = map(int, sys.stdin.readline().split())

    if s == 1:
        if y in male:
            male[y] += 1
        else:
            male[y] = 1
    else:
        if y in female:
            female[y] += 1
        else:
            female[y] = 1

ans = 0
for value in male.values():
    if value > K:
       ans += value // K
       if value % K:
           ans += 1
    else:
        ans += 1

for value in female.values():
    if value > K:
       ans += value // K
       if value % K:
           ans += 1
    else:
        ans += 1

print(ans)