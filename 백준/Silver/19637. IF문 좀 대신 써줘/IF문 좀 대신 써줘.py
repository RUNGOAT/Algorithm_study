import sys
input = sys.stdin.readline


def binary(power):
    s, e = 0, len(arr) - 1
    while s < e:
        mid = (s + e) // 2
        if power > arr[mid][1]:
            s = mid + 1
        else:
            e = mid
    return arr[e][0]


N, M = map(int, input().split())
arr = []
for n in range(N):
    style, power = input().split()
    arr.append((style, int(power)))

for m in range(M):
    power = int(input())
    print(binary(power))
