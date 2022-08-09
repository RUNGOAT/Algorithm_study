for _ in range(10):
    t = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(1, 6):
            if nums[i-1] <= i:
                nums.append(0)
                secret = nums[i:]
                break
            nums.append(nums[i-1] - i)
        nums = nums[i:]
        if nums[-1] == 0:
            break
            
    print(f'#{t}', end=' ')
    print(*secret)
