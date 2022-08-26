def memo(n, m, k, total_time):
    bread = 0
    j = 0
    for i in range(m, total_time + 1):
        if i % m == 0:
            bread += k
 
        fish_bread[i] = bread
 
        if i == people[j]:
            j += 1
            bread -= 1
 
    for i in range(n):
        if fish_bread[people[i]] == 0:
            return "Impossible"
    return "Possible"
 
 
T = int(input())
for tc in range(1, T+1):
    # N : 사람 수, K : M초당 만드는 갯수, M : K개 만드는 시간
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    total_time = max(people)
    people.sort()
    fish_bread = [0] + [0] * total_time
    print(f'#{tc} {memo(N, M, K, total_time)}')