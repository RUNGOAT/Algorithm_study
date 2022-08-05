def d(n):
    for x in list(map(int, str(n))):
        n += x
    return n


numbers = list(range(10000))
for num in range(10000):
    if d(num) in numbers:
        numbers.remove(d(num))
for i in numbers:
    print(i)