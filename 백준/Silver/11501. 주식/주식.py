import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    profit_stock = arr[-1]
    max_profit = 0
    for i in range(N-2, -1, -1):
        if profit_stock > arr[i]:
            max_profit += profit_stock - arr[i]
        else:
            profit_stock = arr[i]
    print(max_profit)
