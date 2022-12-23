import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
ans = int(2e9)
elements = []
s, e = 0, N-1
while s < e:
    ssum = arr[s] + arr[e]

    if abs(ssum) < ans:
        ans = abs(ssum)
        elements = [arr[s], arr[e]]

    if ssum > 0:
        e -= 1
    elif ssum < 0:
        s += 1
    else:
        break

print(elements[0], elements[1])
