import sys
input = sys.stdin.readline


def copy_box(now_box, box, b, t, l, r):
    for j in range(l, r + 1):
        for i in range(b, N):
            now_box[i][j] = box[i][j]


def copy_pointers(now_pointers, l, r):
    for i in range(l, r + 1):
        pointers[i] = now_pointers[i]


def init_box(box, b, t, l, r):
    for j in range(l, r + 1):
        pointer = pointers[j]
        for si in range(b, N):
            i = si
            if box[i][j] == -1:
                flag = True
                while i < N:
                    if box[i][j] != -1:
                        box[si][j] = box[i][j]
                        box[i][j] = -1
                        flag = False
                        break
                    i += 1
                if flag:
                    box[si][j] = arr[pointer][j]
                    pointer += 1
        pointers[j] = pointer


def bfs(sx, sy, visited, box):
    stack = [(sx, sy)]
    visited[sx][sy] = True
    color = box[sx][sy]
    cnt = 1

    min_x = min_y = 16
    max_x = max_y = 0
    while stack:
        x, y = stack.pop()
        box[x][y] = -1
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= N:  continue
            if color != box[nx][ny]:    continue
            if visited[nx][ny]:          continue
            stack.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1

    return cnt + (max_x - min_x + 1) * (max_y - min_y + 1), min_x, max_x, min_y, max_y


def simulation(box, score, round, b, t, l, r):
    global max_score, pointers
    if max_score < score:
        max_score = score

    if round == 4:
        return

    init_box(box, b, t, l, r)

    now_box = [box[i][:] for i in range(N)]
    now_pointers = pointers[:]

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:   continue
            plus, b, t, l, r = bfs(i, j, visited, now_box)

            simulation(now_box, score + plus, round + 1, b, t, l, r)

            copy_pointers(now_pointers, l, r)
            copy_box(now_box, box, b, t, l, r)


N = int(input())
M = 3 * N
temp = [list(map(int, input().split())) for _ in range(M)]
arr = [[] for _ in range(M)]
for i in range(M - 1, -1, -1):
    arr[M - 1 - i] = temp[i]

pointers = [0] * N
box = [[-1] * N for _ in range(N)]
max_score = 0

simulation(box, 0, 1, 0, N-1, 0, N-1)

print(max_score)
