for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    lst = []
    isp = {"*": 2, "+": 1, "(": 0, "-": 1, "/": 2}
    icp = {"*": 2, "+": 1, "(": 3, "-": 1, "/": 2}

    for i in range(N):          # 후위표기법 변환
        if arr[i] in isp:       # 연산자 일 때
            if not stack:
                stack.append(arr[i])
            elif icp[arr[i]] > isp[stack[-1]]:
                stack.append(arr[i])
            else:
                while stack and isp[arr[i]] <= isp[stack[-1]]:
                    lst.append(stack.pop())
                stack.append(arr[i])
        elif arr[i] == ")":
            while stack[-1] != "(":
                lst.append(stack.pop())
            stack.pop()
        else:                   # 숫자일 때
            lst.append(arr[i])
    for _ in range(len(stack)):
        lst.append(stack.pop())

    for i in range(len(lst)):   # 계산
        if lst[i] in isp:
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            if lst[i] == "-":
                stack.append(tmp2 - tmp1)
            elif lst[i] == "+":
                stack.append(tmp2 + tmp1)
            elif lst[i] == "*":
                stack.append(tmp2 * tmp1)
            elif lst[i] == "/":
                stack.append(tmp2 // tmp1)
        else:
            stack.append(lst[i])

    print(f'#{tc} {stack.pop()}')