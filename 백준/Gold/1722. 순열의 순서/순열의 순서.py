import sys
input = sys.stdin.readline


def factorial():
    for i in range(2, N+1):
        memo[i] = memo[i-1] * i


def one_check(num, lst):
    if len(lst) == 1:
        print(lst.pop())
        return
    m = len(lst) - 1
    idx = 0
    while num > memo[m]:
        num -= memo[m]
        idx += 1
    print(lst.pop(idx), end=' ')
    one_check(num, lst)


def two_check(idx, lst):
    global times
    len_lst = len(lst)
    if len_lst == 1:
        print(times)

    for i in range(len_lst):
        if numbers[idx] == lst[i]:
            times += memo[len_lst - 1] * i
            lst.pop(i)
            two_check(idx+1, lst)
            break


N = int(input())
k, *numbers = map(int, input().split())
memo = [1] * (N+1)
factorial()
lst = [i for i in range(1, N+1)]
if k == 1:
    one_check(numbers[0], lst)
else:
    times = 1
    two_check(0, lst)
