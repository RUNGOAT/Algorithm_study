def solution(s):
    global cnt, num
    num += 1
    length = 0
    for i in range(len(s)):
        if s[i] == '1':
            length += 1
        else:
            cnt += 1
    
    s = format(length, 'b')
    if s == '1':
        return [num, cnt]
    else:
        return solution(s)

cnt = num = 0