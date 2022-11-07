import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
left, right = 0, 1
ssum = arr[0]
while left <= right <= N:
    if ssum == M:
        ans += 1
        ssum -= arr[left]
        left += 1
    elif ssum < M:
        if right < N:
            ssum += arr[right]
            right += 1
        else:
            break
    else:
        ssum -= arr[left]
        left += 1
print(ans)