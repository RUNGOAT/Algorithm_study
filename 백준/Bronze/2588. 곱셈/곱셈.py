import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

B = b
while b != 0:
    print(a * (b % 10))
    b //= 10
print(a * B)
