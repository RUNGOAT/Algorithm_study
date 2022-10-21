import sys
input = sys.stdin.readline


def register(a, b):
    q = [[a, '']]
    visited[a] = False
    while True:
        tmp = []
        for a, order in q:
            if a == b:
                return order
            num_d = (a * 2) % 10000
            if visited[num_d]:
                tmp.append([num_d, order + 'D'])
                visited[num_d] = False
            num_s = (a - 1) % 10000
            if visited[num_s]:
                tmp.append([num_s, order + 'S'])
                visited[num_s] = False
            num_l = (a % 1000) * 10 + a // 1000
            if visited[num_l]:
                tmp.append([num_l, order + 'L'])
                visited[num_l] = False
            num_r = (a % 10) * 1000 + a // 10
            if visited[num_r]:
                tmp.append([num_r, order + 'R'])
                visited[num_r] = False
        q = tmp


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [True] * 10000
    print(register(A, B))
