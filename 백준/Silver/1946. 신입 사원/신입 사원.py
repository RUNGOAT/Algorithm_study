import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort()
    ans = 1
    min_v = arr[0][1]
    for i in range(1, N):
        if arr[i][1] < min_v:
            ans += 1
            min_v = arr[i][1]
    print(ans)