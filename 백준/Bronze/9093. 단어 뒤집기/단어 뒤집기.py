T = int(input())
for _ in range(T):
    sentence = list(input().split())
    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]
    print(' '.join(sentence))
