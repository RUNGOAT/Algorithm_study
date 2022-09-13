import sys


def preorder(n):
    if n:
        print(chr(n + 64), end='')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(chr(n + 64), end='')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n + 64), end='')


N = int(sys.stdin.readline())
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
for _ in range(1, N+1):
    v, cl, cr = sys.stdin.readline().split()
    if cl == '.':
        ch1[ord(v) - 64] = 0
    else:
        ch1[ord(v) - 64] = ord(cl) - 64
    if cr == '.':
        ch2[ord(v) - 64] = 0
    else:
        ch2[ord(v) - 64] = ord(cr) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
