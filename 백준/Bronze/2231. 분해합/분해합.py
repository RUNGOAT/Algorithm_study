import sys


def constructor(n):
    tmp = n
    while n > 0:
        tmp += n % 10
        n //= 10
    return tmp


N = int(sys.stdin.readline())

ans = 9999999
for i in range(1, N+1):
    if constructor(i) == N:
        if ans > i:
            ans = i
if ans == 9999999:
    ans = 0

print(ans)
