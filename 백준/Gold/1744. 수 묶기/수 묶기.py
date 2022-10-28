import sys
input = sys.stdin.readline


def minus_sum(lst):
    ssum = 0
    lst.reverse()
    for i in range(0, len(lst), 2):
        if i+1 == len(lst):
            return ssum, lst[-1]
        else:
            ssum += lst[i] * lst[i+1]
    return ssum, 0


N = int(input())
arr = [0] * N
for n in range(N):
    arr[n] = int(input())
arr.sort(reverse=True)
ans = 0
tmp = []
zero_flag = False
i = 0
while i < len(arr):
    if arr[i] == 1:
        ans += 1
        if tmp:
            ans += tmp.pop()
    elif arr[i] == 0:
        # 음수의 갯수가 홀수일 때 마지막 하나만 없애도록
        zero_flag = True
        if tmp:
            ans += tmp.pop()
    elif arr[i] < 0:
        # 음수 의 곱은 양수
        # 음수만 처리할 함수생성
        ssum, last_minus = minus_sum(arr[i:])
        ans += ssum
        if not zero_flag:
            ans += last_minus
        break
    else:
        if tmp:
            ans += tmp.pop() * arr[i]
        else:
            tmp.append(arr[i])
    i += 1
if tmp:
    ans += tmp.pop()
print(ans)
