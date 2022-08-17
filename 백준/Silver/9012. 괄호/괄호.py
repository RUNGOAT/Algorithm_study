import sys


def checking(arr):
    for s in arr:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'


T = int(sys.stdin.readline().strip())
for _ in range(T):
    arr = sys.stdin.readline().strip()
    stack = []
    print(checking(arr))
