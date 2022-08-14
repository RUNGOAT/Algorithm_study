N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    arr = [[1] for _ in range(k+1)]

    for i in range(2, n+1):
        arr[0].append(i)

    for i in range(1, k+1):
        for j in range(1, n):
            arr[i].append(sum(arr[i-1][:j+1]))

    print(arr[k][n-1])
