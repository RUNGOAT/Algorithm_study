import sys
input = sys.stdin.readline


N, M = map(int, input().split())
keywords = set()
for i in range(N):
    keywords.add(input().rstrip())

for i in range(M):
    words = set(input().rstrip().split(","))
    keywords -= words
    print(len(keywords))
