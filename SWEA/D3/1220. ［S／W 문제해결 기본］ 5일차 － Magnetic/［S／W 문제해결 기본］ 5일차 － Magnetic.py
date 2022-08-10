for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stable = 0      # 교착 상태

    for j in range(N):
        lst = []
        for i in range(N):
            if arr[i][j] == 1:
                lst.append('red')
            elif arr[i][j] == 2 and 'red' in lst:
                lst.append('blue')
            if 'red' in lst and 'blue' in lst:
                stable += 1
                lst = []

    print(f'#{tc} {stable}')
