import sys
input = sys.stdin.readline


def f(arr, k):
    if k == N:
        return arr[0][0]

    result = []
    for x in range(0, len(arr), 2):
        temp2 = []
        for y in range(0, len(arr), 2):
            temp = ''
            for i in range(x, x+2):
                for j in range(y, y+2):
                    temp += arr[i][j]

            if temp == '0000':
                temp = '0'
            elif temp == '1111':
                temp = '1'
            else:
                temp = '(' + temp + ')'

            temp2.append(temp)
        result.append(temp2)

    return f(result, k * 2)


N = int(input())
data = [list(input().strip()) for _ in range(N)]
print(f(data, 1))
