def solution(s):
    cnt = num = 0
    while s != '1':
        num += 1
        length = 0
        for i in range(len(s)):
            if s[i] == '1':
                length += 1
            else:
                cnt += 1
        s = format(length, 'b')
    return [num, cnt]