for t in range(1, 11):
    p = int(input())    # palindrome
    board = []
    for i in range(8):
        board.append(list(map(str, input())))
    cnt = 0

    for i in range(8):          # 가로
        for j in range(8-p+1):
            if board[i][j:j+p] == list(reversed(board[i][j:j+p])):
                cnt += 1

    for j in range(8):          # 세로
        for i in range(8-p+1):
            temp = []
            for x in range(p):
                temp.append(board[i+x][j])
            if temp == list(reversed(temp)):
                cnt += 1

    print(f'#{t} {cnt}')
