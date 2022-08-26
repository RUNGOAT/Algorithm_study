T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    # [0] 추가로 열의 끝에서 계산
 
    cnt_dict = {}
    for i in range(N):
        temp = ()
        for j in range(N+1):
            if arr[i][j] != 0:
                temp += (j,)
            else:
                if arr[i][j-1] != 0:
                    if temp in cnt_dict:
                        cnt_dict[temp] += 1
                    else:
                        cnt_dict[temp] = 1
                    temp = ()
 
    print(f'#{tc} {len(cnt_dict)}', end=' ')
    for column, row in sorted(cnt_dict.items(), key=lambda x: (len(x[0]) * x[1], x[1])):
        print(row, len(column), end=' ')
    print()