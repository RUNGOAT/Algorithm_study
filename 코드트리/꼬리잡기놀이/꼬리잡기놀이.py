import sys
input = sys.stdin.readline


def dfs(x, y, numero):
    """
    팀원 위치와 팀 동선 체크
    :param x, y: 머리사람(1)의 위치
    :param numero:  팀 번호
    """
    global search_all_teammate
    move_arr[x][y] = numero      # 팀의 동선 체크
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and move_arr[nx][ny] != numero:
            if arr[nx][ny] == 0:    continue
            if arr[nx][ny] == 2:
                team.append((nx, ny))
            elif arr[x][y] + 1 == 3:
                search_all_teammate = True
                team.append((nx, ny))
            elif not search_all_teammate:  continue     # 팀원 다 찾으면 dfs로 동선만 체크
            dfs(nx, ny, numero)


def head_move(head, numero):
    """
    머리사람이 가야할 곳 체크
    :param head:    머리사람 위치
    :param numero:  팀 번호
    :return:        머리사람이 가야할 위치
    """
    x, y = head
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and move_arr[nx][ny] == numero:
            if arr[nx][ny] == 4 or arr[nx][ny] == 3:    # 동선에 모든 팀원이 존재할 수도 있다.
                return nx, ny


def team_move(numero):
    """
    팀원 위칫값 담은 리스트(total_team) 최신화
    전체 배열(arr) 최신화
    :param numero:   팀 번호
    """
    team = total_team[numero]
    nx, ny = head_move(team[0], numero)
    x, y = team.pop()                            # 꼬리사람 위치
    arr[x][y] = 4                                # 꼬리사람 이동
    for x, y in team:                            # 중간 사람 최신화
        arr[x][y] = 2
    x, y = team[-1]                              # 이동 후 꼬리사람 최신화
    arr[x][y] = 3
    arr[nx][ny] = 1                              # 머리사람 최신화
    total_team[numero] = [(nx, ny)] + team       # 팀 이동 최신화


def ball_check(x, y, d):
    """
    공 던져서 만나는 사람 찾기
    :param x, y:        공의 시작 위치
    :param d:           공 방향 인덱스
    """
    global ans
    for n in range(N):
        if arr[x][y] == 0 or arr[x][y] == 4:
            x += dx[d]
            y += dy[d]
            continue

        numero = move_arr[x][y]     # 팀 번호
        team = total_team[numero]
        for k in range(len(team)):
            if team[k] == (x, y):
                ans += (k + 1) ** 2

                # 머리사람, 꼬리사람 위치 바꾸기
                head_x, head_y = team[0]
                tail_x, tail_y = team[-1]
                arr[head_x][head_y] = 3
                arr[tail_x][tail_y] = 1
                total_team[numero].reverse()
                return


dx = [0, -1, 0, 1]      # 우 상 좌 하
dy = [1, 0, -1, 0]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

numero = 1       # 팀 번호
move_arr = [[0] * N for _ in range(N)]         # 동선 배열이자 방문 체크

total_team = [[0]]                             # 0번 인덱스 사용 안 함
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            search_all_teammate = False        # 팀원 먼저 찾고 동선 체크
            team = [(i, j)]
            dfs(i, j, numero)
            total_team.append(team)
            numero += 1

ans = 0
d = 3       # 공의 시작 위치 설정하기 위한 변수
ball_x = ball_y = 0
n = 0
for k in range(K):

    # 라운드에 따른 공 위치 체크
    if n == N:
        d = (d + 1) % 4
        n = 0
    elif n != 0:
        ball_x += dx[d]
        ball_y += dy[d]

    # 팀의 이동 체크
    for numero in range(1, M+1):
        team_move(numero)

    # 공 던졌을 때 잡는 인원 체크
    # 해당 인원이 팀에서 몇 번째 인지 체크
    # 방향 바꾸기 체크 (팀원을 배열에 담아야 할 듯)
    ball_check(ball_x, ball_y, (d + 1) % 4)

    n += 1      # 라운드 체크

print(ans)
