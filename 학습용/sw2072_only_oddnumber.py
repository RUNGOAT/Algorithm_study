T = int(input())

for t in range(1, T + 1):
    result = 0
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            result += lst[i]
    print(f'#{t} {result}')
