import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    word = input().strip()
    tmp = word[0]
    cnt = 1
    for i in range(1, len(word)):
        if word[i] != tmp:
            cnt += 1
            tmp = word[i]
    if cnt == len(set(word)):
        ans += 1
print(ans)
