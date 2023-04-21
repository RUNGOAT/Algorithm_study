import sys
input = sys.stdin.readline


N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
sushi = [0] * (d + 1)

sushi[c] = 1
for i in range(k):
    sushi[belt[i]] += 1

ans = 0
for i in range(1, d+1):
    if sushi[i] != 0:
        ans += 1

cnt = ans
for i in range(N):
    sushi[belt[i]] -= 1
    if sushi[belt[i]] == 0:
        cnt -= 1
    sushi[belt[(i + k) % N]] += 1
    if sushi[belt[(i + k) % N]] == 1:
        cnt += 1
    ans = max(ans, cnt)

print(ans)
