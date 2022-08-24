T = int(input())
for tc in range(1, T+1):
    dp = [0] * 401
    N = int(input())
    room_list = []
    for n in range(N):
        current, target = map(int, input().split())
        if current > target:
            current, target = target, current
        room_list += [current] + [target]         # n번 학생들의 방 번호 리스트에 담기
        for i in range(current, target+1):
            dp[i] += 1

    for i in range(-1, len(room_list)-1, 2):
        # ex) 1번 학생 target이 3이고, 2번 학생 current가 4인 경우
        if room_list[i] % 2 == 1 and room_list[i+1] == room_list[i] + 1:
            dp[room_list[i]] += 1
            dp[room_list[i+1]] += 1

    print(f'#{tc} {max(dp)}')
