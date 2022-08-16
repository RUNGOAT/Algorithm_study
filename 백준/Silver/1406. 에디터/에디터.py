import sys

stack_l = list(sys.stdin.readline().strip())
stack_r = []
M = int(input())

for _ in range(M):
    command = sys.stdin.readline().split()

    if command[0] == 'L' and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == 'D' and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == 'B' and stack_l:
        stack_l.pop()
    elif command[0] == 'P':
        stack_l.append(command[1])

print(''.join(stack_l + list(reversed(stack_r))))
