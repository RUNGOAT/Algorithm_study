def select_score(i, n, apeach, lion):
    global max_diff, answer
    if n < 0:
        return
    if i == 11:
        if n > 0 :
            lion[10] += n
        diff = cal_score(apeach, lion)
        if max_diff < diff:
            max_diff = diff
            answer = lion[:]
        elif max_diff == diff:
            for i in range(10, -1, -1):
                if answer[i] < lion[i]:
                    answer = lion[:]
                    break
                elif answer[i] > lion[i]:
                    break

        if n > 0:
            lion[10] -= n
    else:
        select_score(i+1, n, apeach, lion)
        if n > apeach[i]:
            lion[i] = apeach[i] + 1
            select_score(i+1, n - (apeach[i] + 1), apeach, lion)
            lion[i] = 0


def cal_score(apeach, lion):
    a_score = b_score = 0
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            a_score += 10-i
        else:
            b_score += 10-i

    return b_score - a_score


def solution(n, info):
    global max_diff, answer
    max_diff = 0
    answer = [0] * 11
    Lion = [0] * 11

    select_score(0, n, info, Lion)

    if max_diff == 0:
        answer = [-1]
    return answer
