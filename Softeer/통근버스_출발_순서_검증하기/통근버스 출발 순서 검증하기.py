import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(N-1):
    tmp = 0
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            tmp += 1
        else:
            ans += tmp
            
print(ans)
