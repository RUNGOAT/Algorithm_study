import sys
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))
ans = [0]

for number in numbers:
    if ans[-1] < number:
        ans.append(number)
    else:
        s = 0
        e = len(ans)
        while s < e:
            mid = (s + e) // 2

            if ans[mid] < number:
                s = mid + 1
            else:
                e = mid
        ans[e] = number

print(len(ans) - 1)
