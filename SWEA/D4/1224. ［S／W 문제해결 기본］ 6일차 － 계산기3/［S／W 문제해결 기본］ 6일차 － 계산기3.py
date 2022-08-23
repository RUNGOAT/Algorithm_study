for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    lst = []
    isp = {"*": 2, "+": 1, "(": 0, "-": 1, "/": 2}
    icp = {"*": 2, "+": 1, "(": 3, "-": 1, "/": 2}

    for i in range(N):
        if arr[i] in isp:
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
        else:
            lst.append(arr[i])
    for _ in range(len(stack)):
        tmp = stack.pop()
        if tmp == "(":
            stack.pop()
        else:
            lst.append(tmp)
    for i in range(len(lst)):
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
