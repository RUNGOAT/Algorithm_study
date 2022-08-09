T = int(input())

for t in range(1, T+1):
    l, u, x = map(int, input().split())
    if x < l:
        print(f'#{t} {l - x}')
    elif x > u:
        print(f'#{t} {-1}')
    else:
        print(f'#{t} {0}')
    