import sys

input = sys.stdin.readline

A = int(input())
s = list(map(int, input().split())) + [0]
stack = [s[0]]
for i in range(1, A):
    if stack[-1] < s[i]:
        stack.append(s[i])
    else:
        j = len(stack) - 1
        while j > 0:
            if stack[j-1] < s[i]:
                break
            j -= 1
        stack[j] = s[i]

print(len(stack))
