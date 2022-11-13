def solution(s):
    answer = 1000
    if len(s) < 3:
        answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        ss = s[:i]
        tmp = ''
        cnt = 0
        for j in range(0, len(s), i):
            if s[j:j+i] == ss:
                cnt += 1
            else:
                if cnt != 1:
                    tmp += str(cnt)
                tmp += ss
                ss = s[j:j+i]
                cnt = 1
        if cnt != 1:
            tmp += str(cnt)
        tmp += ss
        answer = min(answer, len(tmp))

    return answer
