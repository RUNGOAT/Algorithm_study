import sys
input = sys.stdin.readline


def f(k, idx):
    flag = False
    if k == L:
        tmp = []
        for i in range(L):
            if p[i] not in ['a', 'e', 'i', 'o', 'u']:
                tmp.append(p[i])
        if 1 < len(tmp) < L:
            print(''.join(p))
    else:
        for i in range(idx, C-L+1+k):
            p[k] = arr[i]
            f(k+1, i+1)


L, C = map(int, input().split())
arr = sorted(list(input().split()))
p = [''] * L
f(0, 0)
