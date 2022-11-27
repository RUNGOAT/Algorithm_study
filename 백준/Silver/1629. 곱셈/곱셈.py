def power(x, n):
    if n == 0:
        return 1

    y = power(x, n // 2) % C

    if n % 2 == 0:
        return y * y
    else:
        return y * y * x

A, B, C = map(int, input().split())
print(power(A, B) % C)
