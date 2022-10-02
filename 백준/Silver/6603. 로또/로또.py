import sys
input = sys.stdin.readline


def kC6(idx, s):
    if idx == 6:
        print(' '.join(map(str, t)))
    else:
        for i in range(s, k-6+1+idx):
            t[idx] = S[i]
            kC6(idx + 1, i + 1)


t = [0] * 6
while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    kC6(0, 0)
    print()
    