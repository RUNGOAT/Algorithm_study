import sys
input = sys.stdin.readline


def cal(a, oper, b):
    if oper == '*':
        return a * b
    elif oper == '+':
        return a + b
    else:
        return a - b


def dfs(sv, i):
    global ans
    if i == N:
        ans = max(ans, sv)
        return
    v = cal(sv, arr[i], int(arr[i+1]))
    dfs(v, i+2)
    if i != N-2:
        v = cal(int(arr[i+1]), arr[i+2], int(arr[i+3]))
        v = cal(sv, arr[i], v)
        dfs(v, i+4)


N = int(input())
arr = list(input().strip())
ans = int(-1e9)
dfs(int(arr[0]), 1)
print(ans)
