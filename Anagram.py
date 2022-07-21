words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

words_list = []
words_set = {}
words_group = []
words_group_list = []

for i in range(len(words)):
    word = ''.join(sorted(str(words[i])))       # words 리스트의 각 요소 정렬
    words_list.append(word)                     # 정렬한 요소로 리스트 생성

words_set = set(words_list)                     # words_list 내 중복 요소 제거

for word_set in words_set:
    for i in range(len(words_list)):
        if word_set == words_list[i]:
            words_group_list.append(words[i])   # words와 words_list 요소들의 index가 같으므로 원본 단어를 group_list에 대입
    words_group.append(words_group_list)        # 같은 문자열 요소를 지닌 group_list를 group에 대입
    words_group_list = []                       # 다른 문자열 요소를 받기 위해 group_list 초기화

print(words_group)

# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
#
# word = []
#
# for i in range(len(words)):
#     words[i] = list(str(words[i]))
#     words[i].sort()
#     word += [''.join(words[i])]  # set 변환을 위해 join() 사용
#
# word_set = set(word)
# word_list = list(word_set)  # 중복 제거 후 다시 list 변환
#
# grouping = {}
#
# for x in range(len(word_list)):
#     grouping[word_list[x]] = ''  # [word_list[x]] key값에 대입하기 위해 비어있는 value 생성
#     for i in range(len(word)):
#         if word_list[x] == word[i]:
#             grouping[word_list[x]] += word_list[x]
#
# for key, value in grouping.items():
#     print(f'{key} : {value}', end=' / ')
