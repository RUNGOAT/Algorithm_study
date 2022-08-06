T = int(input())

for t in range(1, T + 1):
    test_case = int(input())
    scores = list(map(int, input().split()))
    mode_num = {}
    for score in scores:
        if score in mode_num:
            mode_num[score] += 1
        else:
            mode_num[score] = 1
    mode = sorted(mode_num.items(), key=lambda x: x[1], reverse=True)[0][0]

    print(f'#{t} {mode}')