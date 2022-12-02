import sys
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))

ssum = 0     # 부분합
s = 0        # 부분합의 0번 인덱스
cnt = 0      # 부분합의 원소 갯수
ans = 100000 # 답

for e in range(N):
    ssum += arr[e]
    cnt += 1
    if ssum >= S:
        while ssum >= S:
            ssum -= arr[s]
            cnt -= 1
            s += 1
        if ans > cnt + 1:
            ans = cnt + 1

if ans == 100000:
    print(0)
else:
    print(ans)
