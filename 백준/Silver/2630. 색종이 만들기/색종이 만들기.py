import sys
input = sys.stdin.readline


def check(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != arr[x][y]:
                return False
    return True


def divide(x, y, size):
    if size == 1 or check(x, y, size):
        color[arr[x][y]] += 1
        return
    else:
        size //= 2
        divide(x, y, size)
        divide(x, y + size, size)
        divide(x + size, y, size)
        divide(x + size, y + size, size)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
color = [0, 0]      # white, blue
divide(0, 0, N)
print(color[0])
print(color[1])
