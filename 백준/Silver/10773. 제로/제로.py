import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    k = int(input())
    if k != 0:
        stack.append(k)
    else:
        stack.pop()
print(sum(stack))