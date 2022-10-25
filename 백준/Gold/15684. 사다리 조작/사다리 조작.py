import sys
input = sys.stdin.readline


def ladder_start():
    for sn in range(1, N + 1):
        n = sn
        for h in range(H):
            if arr[h][n - 1]:
                n -= 1
            elif arr[h][n]:
                n += 1
        if sn != n:
            return False
    return True


def manipulate(idx, row_cnt):
    global ans
    if row_cnt > 3 or ans < row_cnt:
        return

    # 모든 가로선 갯수의 합이 짝수이어야 한다.
    if (row_cnt + M) % 2 == 0:
        if ladder_start():  # 사다리 탐색
            ans = min(ans, row_cnt)
            return

    for n in range(idx, N):
        for h in range(H):
            if not arr[h][n] and not arr[h][n-1]:
                arr[h][n] = 1
                manipulate(n, row_cnt + 1)
                arr[h][n] = 0


N, M, H = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a - 1][b] = 1
ans = sys.maxsize
manipulate(0, 0)
if ans > 3:
    ans = -1
print(ans)
