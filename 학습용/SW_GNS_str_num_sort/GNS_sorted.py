def idx_sort(nums_str):
    temp = []
    for i in range(len(nums)):
        temp.append([nums[i], i])

    temp2 = []
    for i in range(int(N)):
        for num in temp:
            if nums_str[i] == num[0]:
                nums_str[i] = [nums_str[i], num[1]]

    result = [x[0] for x in sorted(nums_str, key=lambda x: x[1])]
    return result


nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    nums_str = list(input().split())
    tc = tc.lstrip('#')

    print(f'#{tc}')
    print(' '.join(idx_sort(nums_str)))