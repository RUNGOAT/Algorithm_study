import sys
input = sys.stdin.readline

arr = input().rstrip()
ans = [-1] * 26
for i in range(len(arr)):
    if ans[ord(arr[i]) - 97] == -1:
        ans[ord(arr[i]) - 97] = i
print(' '.join(map(str, ans)))
