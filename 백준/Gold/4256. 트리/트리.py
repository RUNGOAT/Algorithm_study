import sys

def solve(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:
            solve(root + 1, start, i)  # left subtree
            solve(root + 1 + i - start, i + 1, end)  # right subtree
            print(preorder[root], end=" ")


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    solve(0, 0, N)
    print()
