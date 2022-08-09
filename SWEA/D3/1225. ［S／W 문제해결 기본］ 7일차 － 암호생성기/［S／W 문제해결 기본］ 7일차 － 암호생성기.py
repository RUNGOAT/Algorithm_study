for _ in range(10):
    t = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    play = True
    while play:
        for i in range(1, 6):
            if nums[i - 1] <= i:
                nums.append(0)
                secret = nums[i:]
                play = False
                break
            nums.append(nums[i - 1] - i)
        nums = nums[i:]

    print(f'#{t}', end=' ')
    print(*secret)