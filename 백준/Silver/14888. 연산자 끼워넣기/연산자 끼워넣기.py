import sys
from itertools import permutations

read = sys.stdin.readline

N = int(read())
num = list(map(int, read().split()))
opers_tmp = list(map(int, read().split()))
opers = ['+', '-', '*', '/']
opers_list = []
for i in range(4):
    for j in range(opers_tmp[i]):
        opers_list.append(opers[i])

max_ans = -9999999999
min_ans = 9999999999
for oper_list in permutations(opers_list, N - 1):
    i = 1
    result = num[0]
    for oper in oper_list:
        if oper == '+':
            result += num[i]
        elif oper == '-':
            result -= num[i]
        elif oper == '*':
            result *= num[i]
        else:
            if result < 0:
                result *= -1
                result //= num[i]
                result *= -1
            else:
                result //= num[i]
        i += 1
    max_ans = max(result, max_ans)
    min_ans = min(result, min_ans)

print(max_ans)
print(min_ans)
