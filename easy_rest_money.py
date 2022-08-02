T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    rest = N    # divmod 함수에 첫 입력값 할당 후 반복하기 위해 N을 rest에 대입
    print(f'#{t}')
    for m in money:         # quotient == 몫
        quotient, rest = divmod(rest, m)
        print(quotient, end=' ')
    print()