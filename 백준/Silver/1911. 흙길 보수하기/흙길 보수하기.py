import sys
input = sys.stdin.readline


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[0])

answer = 0
start = 0
for i in range(N):
    start = arr[i][0] if arr[i][0] > start else start

    diff = arr[i][1] - start
    remainder = 1

    if arr[i][1] > start:
        if diff % L == 0:
            remainder = 0

        count = diff // L + remainder
        start += count * L
        answer += count

print(answer)