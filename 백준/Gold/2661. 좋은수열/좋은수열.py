import sys
input = sys.stdin.readline


def check(arr):
    for i in range(1, len(arr) // 2 + 1):
        if arr[-i:] == arr[-2 * i: -i]:
            return False
    return True


def sequence(size):
    if size == N:
        print(''.join(ans))
        exit(0)

    for n in range(1, 4):
        ans.append(str(n))
        if check(ans):
            sequence(size + 1)
        ans.pop()


N = int(input())
ans = []
sequence(0)