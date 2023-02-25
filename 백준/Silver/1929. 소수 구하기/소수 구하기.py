import sys, math
input = sys.stdin.readline


def is_prime_num(n):
    arr = [True] * (N+1)
    arr[0] = arr[1] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if arr[i]:
            j = 2

            while (i * j) <= N:
                arr[i * j] = False
                j += 1

    return arr


M, N = map(int, input().split())
arr = is_prime_num(N)
for i in range(M, N+1):
    if arr[i]:
        print(i)
        