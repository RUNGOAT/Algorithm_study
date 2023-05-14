import sys
input = sys.stdin.readline


N = int(input())
length = list(map(int, input().split()))
cities = list(map(int, input().split()))

answer = 0
oil = cities[0]
for i in range(N-1):
    oil = oil if cities[i] > oil else cities[i]
    answer += oil * length[i]

print(answer)
