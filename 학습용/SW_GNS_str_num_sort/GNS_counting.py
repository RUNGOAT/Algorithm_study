def so(nums_str, N):
    temp = []
    for i in range(len(nums)):
        temp.append([nums[i], i])

    cnt = [0] * (len(nums) + 1)
    for s in nums_str:
        for num in temp:
            if s == num[0]:
                cnt[num[1]] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    result = [0] * int(N)
    for i in range(len(result)-1, -1, -1):
        for num in temp:
            if nums_str[i] == num[0]:
                cnt[num[1]] -= 1
                result[cnt[num[1]]] = num[0]

    return result


nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    nums_str = list(input().split())
    tc = tc.lstrip('#')

    print(f'#{tc}')
    print(' '.join(so(nums_str, N)))