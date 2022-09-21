def f(idx, cnt):
    global max_reward
    if cnt == int(K):
        max_reward = max(max_reward, int(''.join(reward)))
    else:
        for i in range(idx, N-1):
            for j in range(i+1, N):
                reward[i], reward[j] = reward[j], reward[i]
                f(i, cnt + 1)
                reward[i], reward[j] = reward[j], reward[i]


T = int(input())
for tc in range(1, T+1):
    reward, K = input().split()
    N = len(reward)
    reward = list(reward)
    max_reward = 0
    f(0, 0)
    print(f'#{tc} {max_reward}')
