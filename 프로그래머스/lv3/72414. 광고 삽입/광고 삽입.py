def to_second(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    play_time = to_second(play_time)
    adv_time = to_second(adv_time)
    time_range = [0] * (play_time + 1)

    for time in logs:
        start, end = time.split('-')
        time_range[to_second(start)] += 1
        time_range[to_second(end)] -= 1
    for i in range(1, play_time):
        time_range[i] += time_range[i-1]

    curr_time = sum(time_range[:adv_time])
    max_time = curr_time
    sec = 0
    for i in range(adv_time, play_time):
        curr_time = curr_time - time_range[i - adv_time] + time_range[i]
        if max_time < curr_time:
            max_time = curr_time
            sec = i - adv_time + 1

    answer = '%02d:%02d:%02d' % (sec/3600, sec/60%60, sec%60)

    return answer
