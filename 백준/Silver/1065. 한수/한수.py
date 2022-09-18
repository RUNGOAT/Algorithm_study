import sys


def num_list(n):
    tmp = []
    while n > 0:
        tmp.append(n % 10)
        n //= 10
    return tmp


N = int(sys.stdin.readline())

ans = 0
for i in range(1, N+1):
    temp = num_list(i)
    list_cnt = len(temp)
    if list_cnt == 1:
        ans += 1
    else:
        flag = True
        diff = temp[0] - temp[1]
        for j in range(1, list_cnt):
            if temp[j-1] - temp[j] != diff:
                flag = False
        if flag:
            ans += 1

print(ans)
