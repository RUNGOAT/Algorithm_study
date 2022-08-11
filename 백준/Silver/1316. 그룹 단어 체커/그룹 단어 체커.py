N = int(input())
ans = 0
for _ in range(N):
    word = input()
    temp = [word[0]]
    for i in range(1, len(word)):
        if word[i] not in temp or word[i] == temp[i-1]:
            temp.append(word[i])
        else:
            break
    else:
        ans += 1

print(ans)
