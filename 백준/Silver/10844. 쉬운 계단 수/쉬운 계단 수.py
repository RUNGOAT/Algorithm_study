import sys
input = sys.stdin.readline


N = int(input())
stairs = [[0] * 10 for _ in range(N+1)]
stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, N+1):
    stairs[i][0] = stairs[i-1][1]
    stairs[i][9] = stairs[i-1][8]
    for j in range(1, 9):
        stairs[i][j] = stairs[i-1][j-1] + stairs[i-1][j+1]

print(sum(stairs[N]) % 1000000000)