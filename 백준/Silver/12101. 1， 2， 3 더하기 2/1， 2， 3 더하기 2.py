import sys
input = sys.stdin.readline


def make_number_sum(i, key, number):
    for num in dic[key]:
        dic[number].append(i + num)


n, k = map(int, input().split())
dic = {1: ['1'], 2: ['11', '2'], 3: ['111', '12', '21', '3']}
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    dic[i] = []
    make_number_sum('1', i - 1, i)
    make_number_sum('2', i - 2, i)
    make_number_sum('3', i - 3, i)

if k > dp[n]:
    print(-1)
    exit(0)

print('+'.join(dic[n][k-1]))
