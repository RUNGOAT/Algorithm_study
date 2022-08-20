import sys

N = int(sys.stdin.readline())

result = []
ans = 0
for num in range(N // 2, N + 1):
    temp = [N, num]
    cnt = 2
    i = 2
    while True:
        if temp[i - 2] - temp[i - 1] < 0:
            break
        temp.append(temp[i - 2] - temp[i - 1])
        cnt += 1
        i += 1
    if ans < cnt:
        ans = cnt
        result = temp

print(ans)
print(*result)
