import sys
N = int(sys.stdin.readline())
hills = []
for _ in range(N):
    hills.append(int(sys.stdin.readline()))
ans = 99999999
for i in range(100-17 + 1):
    tmp = 0
    for j in range(N):
        if hills[j] < i:
            tmp += (i - hills[j]) ** 2
        elif hills[j] > i + 17:
            tmp += (hills[j] - (i + 17)) ** 2
    ans = min(ans, tmp)

print(ans)
