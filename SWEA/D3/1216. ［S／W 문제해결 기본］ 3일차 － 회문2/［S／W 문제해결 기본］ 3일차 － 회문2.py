def max_length(arr):
    for length in range(N, 2, -1):
        for i in range(N):
            for j in range(N - length + 1):
                for k in range(length // 2):
                    if arr[i][j+k] != arr[i][j + (length - 1) - k]:
                        break
                else:
                    return length
 
 
T = 10
N = 100
for tc in range(1, T + 1):
    temp = input()
    arr = [list(input()) for _ in range(N)]
 
    result1 = max_length(arr)
 
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
 
    result2 = max_length(arr)
 
    if result1 < result2:
        result1 = result2
 
    print(f'#{tc} {result1}')