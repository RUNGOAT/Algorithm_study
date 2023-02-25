import sys
input = sys.stdin.readline


def is_prime_num(v):
    if v > max_v:
        for prime_num in prime_list:
            if prime_num >= v:
                break
            elif v % prime_num == 0:
                return False
        return True
    else:
        return arr[v]


# 에라토스테네스의 체
max_v = 2000001
arr = [True] * max_v
arr[0] = arr[1] = False

prime_list = []
for i in range(2, max_v):
    if arr[i]:
        prime_list.append(i)

        j = 2
        while (i * j) <= max_v - 1:
            arr[i * j] = False
            j += 1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    ssum = A + B
    if ssum < 4:
        print('NO')
    elif ssum % 2 == 0:
        print('YES')
    elif is_prime_num(ssum - 2):
        print('YES')
    else:
        print('NO')
