T = int(input())

for t in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    prices.reverse()
    max_price = prices[0]
    for i in prices:
        if i > max_price:
            max_price = i
        else:
            profit += max_price - i

    print(f'#{t} {profit}')