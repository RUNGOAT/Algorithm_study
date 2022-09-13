import sys


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


N = int(sys.stdin.readline())
tree = {}
for _ in range(1, N+1):
    node, cl, cr = sys.stdin.readline().split()
    tree[node] = [cl, cr]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
