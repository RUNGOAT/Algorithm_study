import sys
input = sys.stdin.readline


def check(t, s):
    for i in range(len(t)):
        if t[i] != s[i]:
            return False
    return True


def dfs():
    if len(T) == len(S):
        if check(T, S):
            print(1)
            exit(0)
        return

    if T[len(T) - 1] == 'A':
        T.pop()
        dfs()
        T.append('A')

    if T[0] == 'B':
        T.reverse()
        T.pop()
        dfs()
        T.append('B')
        T.reverse()


S = list(input().rstrip())
T = list(input().rstrip())
dfs()
print(0)