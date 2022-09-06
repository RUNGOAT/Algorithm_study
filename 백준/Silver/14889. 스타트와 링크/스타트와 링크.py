import sys
from itertools import combinations

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

people = list(range(N))
ans = 9999999999

for team in combinations(people, N//2):
    s_team = l_team = 0
    tmp = []
    for i in people:
        if i not in team:
            tmp.append(i)

    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                s_team += S[team[i]][team[j]]
                l_team += S[tmp[i]][tmp[j]]

    temp = abs(s_team - l_team)
    if ans > temp:
        ans = temp

print(ans)
