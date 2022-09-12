def solution(s):
    number = list(map(int, s.split()))
    max_ans = min_ans = number[0]
    for i in range(1, len(number)):
        if max_ans < number[i]:
            max_ans = number[i]
        if min_ans > number[i]:
            min_ans = number[i]
    return " ".join(map(str, [min_ans, max_ans]))
