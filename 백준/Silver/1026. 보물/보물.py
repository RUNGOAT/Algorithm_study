import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
tmp = sorted(enumerate(B), key=lambda x: x[1], reverse=True)
ans = 0
for i in range(N):
    ans += (A[i] * tmp[i][1])
print(ans)
