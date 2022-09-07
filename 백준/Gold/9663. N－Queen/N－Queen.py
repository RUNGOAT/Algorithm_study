import sys


def possible(k):       # k행에서 퀸을 둘 수 있는 인덱스 리스트 반환
    temp = [0] * N
    if stack:
        for i, j in stack:
            for dj in [-1, 0, 1]:
                nj = j + dj * (k-i)     # k행에서 i번째 퀸의 공격 범위에 들어가는 인덱스
                if 0 <= nj < N:
                    temp[nj] = 1

    lst = []
    for i in range(N):
        if temp[i] == 0:        # 앞서 놓은 퀸들의 공격 범위에 들어가지 않는다면
            lst.append(i)
    return lst


def n_queen(k, cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    else:
        possible_list = possible(k)
        for j in possible_list:
            stack.append([k, j])
            n_queen(k+1, cnt+1)
            stack.pop()


N = int(sys.stdin.readline())
ans = 0
stack = []      # 퀸을 놓는 위칫값을 담는 리스트
n_queen(0, 0)
print(ans)
