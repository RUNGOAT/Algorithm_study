import sys


def inorder(n):
    if n < 2**N:
        inorder(n*2)
        in_tree.append(n)
        inorder(n*2 + 1)


N = int(sys.stdin.readline())
in_result = list(map(int, sys.stdin.readline().split()))
in_tree = []
inorder(1)
result = sorted(zip(in_tree, in_result))
result = [0] + result
for i in range(N):
    for j in range(2**i, 2**(i+1)):
        print(result[j][1], end=' ')
    print()
