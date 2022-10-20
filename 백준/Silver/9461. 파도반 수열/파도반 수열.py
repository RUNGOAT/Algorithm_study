import sys
input = sys.stdin.readline

P = [0] * 101
P[1], P[2], P[3], P[4], P[5] = 1, 1, 1, 2, 2
for i in range(5, 100):
    P[i+1] = P[i] + P[i-4]

T = int(input())
for _ in range(T):
    N = int(input())
    print(P[N])