import sys
input = sys.stdin.readline


N = int(input())
first_word = list(input())
ans = 0
for _ in range(1, N):
    word = list(input())
    cnt = 0
    compare = first_word[:]
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt <= 1 and len(compare) <= 1:
        ans += 1

print(ans)
