T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    for n in range(N):      # 입력값을 받아 2차원 배열 생성
        puzzle.append(list(map(int, input().split())))

    result = 0
    for i in range(N):      # 가로줄 탐색
        total = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                total += 1
            if puzzle[i][j] == 0 or j == N-1:
                if total == K:
                    result += 1
                    total = 0
                else:
                    total = 0
    
    for j in range(N):      # 세로줄 탐색
        total = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                total += 1
            if puzzle[i][j] == 0 or i == N-1:
                if total == K:
                    result += 1
                    total = 0
                else:
                    total = 0
    
    print(f'#{t} {result}')