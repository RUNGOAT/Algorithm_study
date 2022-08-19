def dfs(index, cnt):
    global result
    if cnt == count:
        result = max(int(''.join(reward)), result)
        return

    for i in range(index, N):
        for j in range(i+1, N):
            if reward[i] <= reward[j]:
                reward[i], reward[j] = reward[j], reward[i]
                dfs(i, cnt+1)
                reward[j], reward[i] = reward[i], reward[j]

    if result == 0 and cnt < count:
        if (count - cnt) % 2:
            reward[-1], reward[-2] = reward[-2], reward[-1]
        dfs(index, count)


T = int(input())
for tc in range(1, T+1):
    reward, count = input().split()
    reward = list(reward)
    N = len(reward)
    count = int(count)
    result = 0
    dfs(0, 0)

    print(f'#{tc} {result}')
