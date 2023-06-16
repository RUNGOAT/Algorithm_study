def solution(lottos, win_nums):
    answer = []
    zero_cnt = 0
    equal_numbers = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
            continue
        if lotto in win_nums:
            equal_numbers += 1
            
    answer.append(check_rank(equal_numbers + zero_cnt))
    answer.append(check_rank(equal_numbers))
    return answer


def check_rank(equal_numbers):
    if equal_numbers == 6:
        return 1
    if equal_numbers == 5:
        return 2
    if equal_numbers == 4:
        return 3
    if equal_numbers == 3:
        return 4
    if equal_numbers == 2:
        return 5
    return 6