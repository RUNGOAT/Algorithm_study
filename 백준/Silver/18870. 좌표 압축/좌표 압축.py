import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))
dic = {}
for i in range(len(sort_arr)):
    dic[sort_arr[i]] = i

for n in range(N):
    print(dic[arr[n]], end=' ')
    