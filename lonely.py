'''
정수 0부터 9까지로 이루어진 list를 전달 받아,
연속적으로 나타나는 숫자는 하나만 남 기고 제거한 list를 반환하는 lonely 함수를 작성하시오.
이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다
'''

def lonely(lst):
    lone = set()
    lst2 = []
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            if lst[0] != lst[1]:
                lone.add(lst[0])            # 첫 번째 값이 연속되지 않으면 바로 lone에 추가
            lst2.append(list(lone)[0])      # set타입의 lone에 저장된 값 하나를 lst2에 대입
            lone = set()                    # 대입하고 초기화
            lone.add(lst[i+1])              # 초기화 후 다음 숫자 대입
            if i+1 == len(lst)-1:           # 연속되지 않은 다음 숫자가 마지막이라면
                lst2.append(lst[i+1])       # 바로 lst2에 대입
        else:
            lone.add(lst[i])
            if i == len(lst) - 2:           # 연속되는 숫자가 마지막이라면
                lst2.append(list(lone)[0])  # 바로 lst2에 대입
    return lst2

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))


'''
아래가 간단
i + 1 로 가는 방법과 i - 1로 가는 방법은 다르게 풀 수 있다.
첫 문자를 대입하고 시작
'''
# def lonely(numbers):
#     result = []

#     result.append(numbers[0])

#     for i in range(1, len(numbers)):
#         if numbers[i] != numbers[i - 1]:
#             result.append(numbers[i])

#     return result


# lonely([1, 1, 3, 3, 0, 1, 1])
# lonely([4, 4, 4, 3, 3])