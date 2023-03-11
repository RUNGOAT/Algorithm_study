import sys
input = sys.stdin.readline


def dfs(x, cnt, time):
    global min_time

    if cnt == N:
        min_time = min(min_time, time)
        return

    for nx in range(N):
        if not visited[nx]:
            visited[nx] = True
            dfs(nx, cnt + 1, time + arr[x][nx])
            visited[nx] = False


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 플로이드-워셜. 모든 정점 최단 거리 구하기
for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

visited = [False] * N
min_time = int(1e9)
visited[K] = True

dfs(K, 1, 0)
print(min_time)