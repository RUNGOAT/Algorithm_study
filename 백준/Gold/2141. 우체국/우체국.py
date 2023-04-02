import sys
input = sys.stdin.readline


N = int(input())
villege = []
total = 0
for _ in range(N):
    x, a = map(int, input().split())
    villege.append((x, a))
    total += a
villege.sort(key=lambda x: x[0])
ssum = 0
half = (total + 1) // 2
for n in range(N):
    x, a = villege[n]
    ssum += a
    if ssum >= half:
        print(x)
        break
