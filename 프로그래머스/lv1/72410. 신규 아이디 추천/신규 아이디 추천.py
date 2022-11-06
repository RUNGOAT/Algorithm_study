def solution(new_id):
    answer = ''
    remove_str = '~!@#$%^&*()=+[{]}:?,<>/'
    # 1.
    new_id = new_id.lower()
    # 2.
    new_id = list(new_id)
    for i in range(len(new_id)):
        if new_id[i] in remove_str:
            new_id[i] = ''
    new_id = list(''.join(new_id))
    # 3.
    flag = False
    for i in range(len(new_id)):
        if new_id[i] == '.':
            if flag:
                new_id[i] = ''
            else:
                flag = True
        else:
            flag = False
    # 4.
    answer = ''.join(new_id)
    answer = answer.strip('.')
    # 5.
    if answer == '':
        answer = 'a'
    # 6.
    answer = answer[:15]
    answer = answer.rstrip('.')
    # 7.
    while len(answer) < 3:
        answer += answer[-1]
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("a.$.a"))


