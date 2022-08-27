import sys

N = int(sys.stdin.readline())
pillar = []
for _ in range(N):
    l, h = map(int, sys.stdin.readline().split())
    pillar += [[l] + [h]]
pillar.sort()
ans = 0

stack = [pillar[0]]
for i in range(1, N):
    if stack[-1][1] <= pillar[i][1]:
        stack.append(pillar[i])

max_h_idx = pillar.index(stack[-1])
ans += pillar[max_h_idx][1]

temp = []
if max_h_idx != N-1:
    temp.append(pillar[N-1])
for i in range(N-2, max_h_idx, -1):
    if temp[-1][1] <= pillar[i][1]:
        temp.append(pillar[i])

stack += reversed(temp)
stack.append([0, 0])
for i in range(1, len(stack)):
    if stack[i-1][1] <= stack[i][1]:
        ans += abs(stack[i][0] - stack[i-1][0]) * stack[i-1][1]
    else:
        ans += abs(stack[i][0] - stack[i-1][0]) * stack[i][1]

print(ans)
