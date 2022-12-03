import sys
input = sys.stdin.readline


def f(i, energy, pleasure, r_L, r_J):
    global max_pleasure
    if energy < 1:
        if max_pleasure < pleasure - J[i-1]:
            max_pleasure = pleasure - J[i - 1]
        return
    if r_J + pleasure <= max_pleasure:  return
    if energy - r_L > 0:
        if max_pleasure < pleasure + r_J:
            max_pleasure = pleasure + r_J
        return
    f(i + 1, energy - L[i], pleasure + J[i], r_L - L[i], r_J - J[i])
    f(i + 1, energy, pleasure, r_L - L[i], r_J - J[i])


N = int(input())    # 사람 수
L = list(map(int, input().split()))    # 잃는 체력
J = list(map(int, input().split()))    # 얻는 기쁨
visited = [False] * N                  # 방문 체크
max_pleasure = 0                       # 최대 기쁨
f(0, 100, 0, sum(L), sum(J))
print(max_pleasure)
