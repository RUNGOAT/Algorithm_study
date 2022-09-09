import sys
from copy import deepcopy


def bfs(i, j):
    q = [[i, j]]
    arr1[i][j] = ''
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr1[ni][nj] != '' and arr1[ni][nj] not in color:
                q.append([ni, nj])
                arr1[ni][nj] = ''


def bfs2(i, j):
    q = [[i, j]]
    arr2[i][j] = ''
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr2[ni][nj] != '' and arr2[ni][nj] not in color:
                q.append([ni, nj])
                arr2[ni][nj] = ''


N = int(sys.stdin.readline())
arr1 = [list(sys.stdin.readline().strip()) for _ in range(N)]
arr2 = deepcopy(arr1)
ans1 = ans2 = 0
color = ['R', 'G', 'B']

for i in range(N):
    for j in range(N):
        if arr1[i][j] == 'R' or arr1[i][j] == 'G' or arr1[i][j] == 'B':
            tmp = arr1[i][j]
            color.remove(tmp)
            bfs(i, j)
            color.append(tmp)
            ans1 += 1

        if arr2[i][j] != '':
            if arr2[i][j] == 'B':
                tmp2 = ['B']
                color.remove('B')
            else:
                tmp2 = ['R', 'G']
                color.remove('R')
                color.remove('G')
            bfs2(i, j)
            color += tmp2
            ans2 += 1

print(ans1, ans2)
