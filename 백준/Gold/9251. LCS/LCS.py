import sys
input = sys.stdin.readline

arr1 = [''] + list(input().strip())
arr2 = [''] + list(input().strip())
LCS = [[0] * (len(arr2)) for _ in range(len(arr1))]

for i in range(1, len(arr1)):
    for j in range(1, len(arr2)):
        if arr1[i] == arr2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[len(arr1)-1][len(arr2)-1])