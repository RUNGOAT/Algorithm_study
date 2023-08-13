nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    nums_str = list(input().split())
    tc = tc.lstrip('#')

    result = []
    for num in nums:
        for num_str in nums_str:
            if num == num_str:
                result.append(num)

    print(f'#{tc}')
    print(' '.join(result))