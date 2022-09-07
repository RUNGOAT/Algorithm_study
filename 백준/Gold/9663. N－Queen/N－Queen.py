import sys


def check(k):
    temp = [0] * N
    if stack:
        for i, j in stack:
            for dj in [-1, 0, 1]:
                nj = j + dj * (k-i)
                if 0 <= nj < N:
                    temp[nj] = 1

    lst = []
    for i in range(N):
        if temp[i] == 0:
            lst.append(i)
    return lst


def f(k, cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    else:
        check_list = check(k)
        for j in check_list:
            stack.append([k, j])
            f(k+1, cnt+1)
            stack.pop()


N = int(sys.stdin.readline())
ans = 0
stack = []
f(0, 0)
print(ans)
