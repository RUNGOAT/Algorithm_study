import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [[0] * (N+1)]
for n in range(N):
    arr.append([0] + list(map(int, input().split())))

# 행의 합
for i in range(1, N+1):
    for j in range(1, N):
        arr[i][j+1] += arr[i][j]

# 열의 합
for j in range(1, N+1):
    for i in range(1, N):
        arr[i+1][j] += arr[i][j]

# 구간합
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    section_sum = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(section_sum)
