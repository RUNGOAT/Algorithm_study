N = int(input())

temp = []

if N % 5 == 0:
    temp.append((N // 5))
else:
    i = 0
    while N - 5 * i > 0:
        if (N - 5 * i) % 3 == 0:
            temp.append((N - 5 * i) // 3 + i)
        i += 1

if len(temp) == 0:
    print(-1)
else:
    print(min(temp))
