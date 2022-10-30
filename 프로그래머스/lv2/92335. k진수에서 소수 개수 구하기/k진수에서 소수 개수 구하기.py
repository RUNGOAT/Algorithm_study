import math
def ntok(n, k):
    lst = []
    while n > 0:
        lst.append(n % k)
        n //= k
    return list(reversed(lst))


def is_primenumber(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_num = ntok(n, k) + [0]
    prime = []
    for num in k_num:
        if num == 0:
            if prime and is_primenumber(int(''.join(map(str, prime)))):
                answer += 1
            prime.clear()
        else:
            prime.append(num)
    return answer
