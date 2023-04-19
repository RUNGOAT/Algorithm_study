import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = set()
for i in range(N):
    arr.add(input().rstrip())

for i in range(M):
    keywords = input().rstrip().split(",")
    for word in keywords:
        try:
            arr.remove(word)
        except:
            pass
    print(len(arr))
