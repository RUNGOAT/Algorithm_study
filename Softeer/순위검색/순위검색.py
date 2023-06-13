import sys
input = sys.stdin.readline


def calculate_ranks(arr):
    tmp = tuple(map(int, input().split()))
    for i in range(N):
        people[i] = (tmp[i], i)
        total[i] += tmp[i]

    assign_rank(people, arr)

    print(' '.join(map(str, arr)))


def calculate_final_ranks(total, arr):
    for i in range(N):
        people[i] = (total[i], i)

    assign_rank(people, arr)

    print(' '.join(map(str, arr)))


def assign_rank(people, arr):
    people.sort(key=lambda x: x[0], reverse=True)

    size = 1
    rank = 1
    stack = people[0][0]
    arr[people[0][1]] = rank

    for i in range(1, N):
        if people[i][0] < stack:
            rank += size
            size = 1
            stack = people[i][0]
        else:
            size += 1
        arr[people[i][1]] = rank


N = int(input())
total = [0] * N
arr = [0] * N
people = [0] * N

for i in range(3):
    calculate_ranks(arr)
calculate_final_ranks(total, arr)
