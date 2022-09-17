import sys


def binary(s, e, target):
    while s <= e and N_arr[s] <= N_arr[e]:
        mid = (s + e) // 2
        if N_arr[mid] == target:
            return 1
        elif N_arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return 0


N = int(sys.stdin.readline())
N_arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    print(binary(0, N-1, M_arr[i]))
