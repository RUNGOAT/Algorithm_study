import sys
input = sys.stdin.readline


def is_ate(idx):
    s = 0 if idx - K < 0 else idx - K
    e = idx + K if idx + K < N else N - 1
    for i in range(s, e+1):
        if line[i] == 'H':
            line[i] = 'X'
            return True
    return False


N, K = map(int, input().split())
line = list(input().rstrip())

ans = 0
for i in range(N):
    if line[i] == 'P' and is_ate(i):
        ans += 1

print(ans)
