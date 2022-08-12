N, K = map(int, input().split())

N = list(range(1, N + 1))
idx = K - 1
josephus = []
while True:
    josephus.append(N.pop(idx))
    if len(N) == 0:
        break
    idx += K-1
    while idx >= len(N):
        idx -= len(N)

print("<" + ", ".join(list(map(str, josephus))) + ">")
