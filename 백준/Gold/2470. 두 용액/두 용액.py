import sys
input = sys.stdin.readline


N = int(input())
arr = sorted(list(map(int, input().split())))

value = abs(arr[1] + arr[0])
answer = (arr[0], arr[1])
s, e = 0, N-1

while s < e:
    ssum = arr[s] + arr[e]

    if abs(ssum) < value:
        value = abs(ssum)
        answer = (arr[s], arr[e])

    if ssum < 0:
        s += 1
    else:
        e -= 1

print(' '.join(map(str, sorted(answer))))
