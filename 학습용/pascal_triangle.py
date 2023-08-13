T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    numbers = [[1]]         # 첫 줄에 1을 대입하고 시작
    for n in range(2, N + 1):
        lst = []
        lst.append(1)       # 각 줄의 시작과 끝은 1로 고정
        for i in range(n):
            if i+1 < n-1:
                lst.append(numbers[n-2][i] + numbers[n-2][i+1])     # n-2 == 이전 줄
            else:
                break
        lst.append(1)       # 각 줄의 시작과 끝은 1로 고정
        numbers.append(lst)
 
    print(f'#{t}')
    for i, k in enumerate(numbers):    
        print(*k)

# 애스터리스크(*) 활용