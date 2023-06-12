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



print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))