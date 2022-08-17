import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = list(range(1, n+1))
    for _ in range(k):
        for i in range(1, n):
            people[i] = people[i-1] + people[i]
    print(people[n-1])
