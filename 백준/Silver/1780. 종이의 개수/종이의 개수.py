import sys
input = sys.stdin.readline


def check(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != arr[x][y]:
                return False
    return True


def divide(x, y, size):
    if size == 1 or check(x, y, size):
        paper[arr[x][y]] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                divide(x + i * size, y + j * size, size)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paper = [0, 0, 0]
divide(0, 0, N)
print(paper[-1])
print(paper[0])
print(paper[1])
