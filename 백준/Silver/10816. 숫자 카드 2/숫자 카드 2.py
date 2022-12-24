import sys
input = sys.stdin.readline


N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))
dic = {}
for n in arrN:
    if dic.get(n, 0):
        dic[n] += 1
    else:
        dic[n] = 1

for m in arrM:
    print(dic.get(m, 0), end=' ')
