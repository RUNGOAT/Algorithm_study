import sys
input = sys.stdin.readline


def f(x, y, size, num):
    if not (x <= r < x + size and y <= c < y + size):
        return
    if size == 2:
        for i in range(x, x + size):
            for j in range(y, y + size):
                if i == r and j == c:
                    print(num)
                    exit(0)
                num += 1
    else:
        size //= 2
        f(x, y, size, num)
        f(x, y + size, size, num + size**2)
        f(x + size, y, size, num + size**2 * 2)
        f(x + size, y + size, size, num + size**2 * 3)


N, r, c = map(int, input().split())
f(0, 0, 2**N, 0)
