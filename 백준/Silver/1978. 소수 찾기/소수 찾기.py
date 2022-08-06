import sys

def f(lst):
    numbers = list(range(2, 1001))
    result = 0
    for i in range(3, 1001):
        for j in range(2, i):
            if i % j == 0:
                if i in numbers:
                    numbers.remove(i)
                    break
    for i in lst:
        if i in numbers:
            result += 1
    return result

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

print(f(num_list))
