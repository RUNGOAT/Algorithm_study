import sys

def f(lst):
    result = N
    for i in lst:
        for j in range(2, i):
            if i % j == 0:
                result -= 1
                break
        if i == 1:
            result -= 1
    return result

N = int(input())

print(f(list(map(int, sys.stdin.readline().split()))))
