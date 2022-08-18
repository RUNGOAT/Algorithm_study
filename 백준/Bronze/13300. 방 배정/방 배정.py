import sys

N, K = map(int, sys.stdin.readline().split())

student_dict = {}
for i in range(N):
    student = tuple(sys.stdin.readline().split())
    if student in student_dict:
        student_dict[student] += 1
    else:
        student_dict[student] = 1

ans = 0
for value in student_dict.values():
    if value > K:
        ans += (value // K)
        if value % K:
            ans += 1
    else:
        ans += 1

print(ans)

