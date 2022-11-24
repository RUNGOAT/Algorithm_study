import sys
input = sys.stdin.readline

N = int(input())
num = [0] * 10001
for _ in range(N):
    n = int(input())
    num[n] += 1

for n in range(10001):
    for _ in range((num[n])):
        print(n)
        