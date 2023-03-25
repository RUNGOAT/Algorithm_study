import sys
input = sys.stdin.readline


def guard_check(x, y, person_num):
    """방역 좌석 체크

    :param x, y: 사람이 앉은 자리
    :param person_num:
         방역 좌석 -1을 해준다. (In일 경우)
         사람이 식사 후 나가면 +1을 하여 방역 좌석 체크
    :return:
    """
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            arr[nx][ny] += person_num


def search_seat(id):
    """좌석 탐색

    :param id: 사원 id
    :return: 상황에 맞는 문구 출력
    """
    tx = ty = D = 0
    for x in range(N):
        for y in range(M):
            min_d = 1000
            if arr[x][y] == 0:
                # 안전도 체크
                for xi, yi, ate in employee.values():
                    if ate:     continue
                    d = ((xi - x) ** 2 + (yi - y) ** 2) ** 1 / 2
                    if min_d > d:
                        min_d = d

                # 최대 안전도 체크
                if D < min_d:
                    tx, ty = x, y
                    D = min_d

    if arr[tx][ty] != 0:
        # 자리 없음
        return f'There are no more seats.'
    employee[id] = (tx, ty, False)
    arr[tx][ty] = id
    guard_check(tx, ty, -1)
    # 착석
    return f'{id} gets the seat ({tx + 1}, {ty + 1}).'


N, M, Q = map(int, input().split())
arr = [[0] * M for _ in range(N)]
employee = {}      # {id : (x, y, ate), ...}
'''
ate == False: 식사 중인 상태
ate == True: 식사 완료 상태
'''
for _ in range(Q):
    q, id = input().split()
    id = int(id)
    if q == 'Out':
        if id not in employee:     # 아직 점심을 먹지 않은 경우
            print(f"{id} didn't eat lunch.")
        else:
            x, y, ate = employee[id]
            if ate:
                # 이미 식사를 한 경우
                print(f'{id} already left seat.')
            else:
                # 식사 중인 경우
                print(f'{id} leaves from the seat ({x + 1}, {y + 1}).')
                employee[id] = (x, y, True)
                arr[x][y] = 0
                guard_check(x, y, 1)
    else:  # In
        if id not in employee:
            # 첫 방문
            print(search_seat(id))
        else:
            x, y, ate = employee[id]
            if ate:
                # 이미 식사를 한 경우
                print(f'{id} already ate lunch.')
            else:
                # 식사 중인 경우
                print(f'{id} already seated.')
