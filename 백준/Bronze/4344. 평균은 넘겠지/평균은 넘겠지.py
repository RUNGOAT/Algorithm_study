C = int(input())
for c in range(C):
    num = list(map(int, input().split()))
    scores = num[1:len(num)]
    average = sum(scores) // num[0]
    result = 0
    for score in scores:
        if score > average:
            result += 1

    print(f'{round((result / num[0]) * 100, 3):.3f}%')
    