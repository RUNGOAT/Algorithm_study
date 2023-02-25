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
    elif ssum % 2 == 0:    #합이 4이상이고 짝수면 무조건 소수로 분리가 가능하다(골드바흐의 추측)
        print('YES')
    elif is_prime_num(ssum - 2):    # 이외의 숫자는 소수 2와 홀수 소수의 조합으로만 가능하여 합-2가 소수인지 판별하면 된다.
        print('YES')
    else:
        print('NO')
