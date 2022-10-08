import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
break_nums = list(map(int, input().split()))
ans = abs(N - 100)
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if int(num[j]) in break_nums:
            break
        elif j == len(num) - 1:
            ans = min(ans, abs(int(num) - N) + len(num))
print(ans)