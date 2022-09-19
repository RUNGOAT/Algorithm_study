import sys
read = sys.stdin.readline


def dfs(result, i, plus, minus, multi, div):
    global max_ans, min_ans
    if i == N:
        max_ans = max(result, max_ans)
        min_ans = min(result, min_ans)
    else:
        if plus:
            dfs(result + num[i], i + 1, plus - 1, minus, multi, div)
        if minus:
            dfs(result - num[i], i + 1, plus, minus - 1, multi, div)
        if multi:
            dfs(result * num[i], i + 1, plus, minus, multi - 1, div)
        if div:
            dfs(int(result / num[i]), i + 1, plus, minus, multi, div - 1)


N = int(read())
num = list(map(int, read().split()))
opers_tmp = list(map(int, read().split()))

max_ans = -9999999999
min_ans = 9999999999

dfs(num[0], 1, opers_tmp[0], opers_tmp[1], opers_tmp[2], opers_tmp[3])

print(max_ans)
print(min_ans)
