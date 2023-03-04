def dfs(sheep, wolf, edges, visited, info):
    global answer
    if sheep > wolf:
        answer.append(sheep)
    else:
        return
    
    for p, c in edges:
        if visited[p] and not visited[c]:
            visited[c] = True
            if info[c] == 0:
                dfs(sheep + 1, wolf, edges, visited, info)
            else:
                dfs(sheep, wolf + 1, edges, visited, info)
            visited[c] = False


def solution(info, edges):
    global answer
    visited = [False] * len(info)
    answer = []
    visited[0] = True
    dfs(1, 0, edges, visited, info)
    
    return max(answer)
