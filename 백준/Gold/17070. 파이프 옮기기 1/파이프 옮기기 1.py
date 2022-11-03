import sys
input = sys.stdin.readline


def dfs(dir, ex, ey):
    global ans
    if ex == N-1 and ey == N-1:
        ans += 1
        return

    if dir == 1 or dir == 3:
        ny = ey + 1
        if ny < N and not arr[ex][ny]:
            dfs(1, ex, ey + 1)
    if dir == 2 or dir == 3:
        nx = ex + 1
        if nx < N and not arr[nx][ey]:
            dfs(2, ex+1, ey)
    nx, ny = ex + 1, ey + 1
    if nx < N and ny < N and not arr[nx][ey] and not arr[ex][ny] and not arr[nx][ny]:
        dfs(3, ex + 1, ey + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(1, 0, 1)
print(ans)
