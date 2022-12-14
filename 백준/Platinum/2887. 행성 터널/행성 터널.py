import sys
input = sys.stdin.readline


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


# 좌표를 x,y,z 별로 저장하고 정렬
N = int(input())
xlst, ylst, zlst = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    xlst.append((x, i))
    ylst.append((y, i))
    zlst.append((z, i))
xlst.sort()
ylst.sort()
zlst.sort()

# 인접한 행성들끼리 간선 구성
edges = []
for curList in xlst, ylst, zlst:
    for i in range(1, N):
        w1, a = curList[i - 1]
        w2, b = curList[i]
        edges.append((abs(w1 - w2), a, b))
edges.sort(reverse=True)

# 크루스칼 진행
p = [i for i in range(N + 1)]
cnt, ans = N - 1, 0
while cnt:
    w, a, b = edges.pop()
    A = find_set(a)
    B = find_set(b)
    if A == B:
        continue
    p[B] = A
    cnt -= 1
    ans += w
print(ans)
