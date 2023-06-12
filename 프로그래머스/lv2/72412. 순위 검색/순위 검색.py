def binary(lst, target):
    s = 0
    e = len(lst)
    
    while s < e:
        mid = (s + e) // 2
        if lst[mid] < target:
            s = mid + 1
        else:
            e = mid
    
    return s


def dfs(dic, depth, condition, idx):
    global answer
    if depth == 4:
        score = condition[depth]
        s = binary(dic, score)
        answer[idx] += len(dic) - s
        return
    
    if condition[depth] == '-':
        for key in dic.keys():
            dfs(dic[key], depth + 1, condition, idx)
    else:
        dfs(dic[condition[depth]], depth + 1, condition, idx)
            

def solution(info, query):
    global answer, dic
    answer = [0] * len(query)
    language = ['cpp', 'java', 'python']
    job = ['backend', 'frontend']
    career = ['junior', 'senior']
    food = ['chicken', 'pizza']
    
    dic = {}
    for l in language:
        dic[l] = {}
        for j in job:
            dic[l][j] = {}
            for c in career:
                dic[l][j][c] = {}
                for f in food:
                    dic[l][j][c][f] = []
                
    for i in range(len(info)):
        l, j, c, f, score = info[i].split()
        dic[l][j][c][f].append(int(score))
    
    for l in language:
        for j in job:
            for c in career:
                for f in food:
                    dic[l][j][c][f].sort()
        
    for i in range(len(query)):
        query[i] = list(query[i].split())
        condition = [query[i][0], query[i][2], query[i][4], query[i][6], int(query[i][7])]
        dfs(dic, 0, condition, i)
        
    return answer