import sys


def print_20(arr):
    i = 0
    while True:
        for j in range(20*i, 20*(i+1)):
            print(switch[j], end=' ')
            if j + 1 == N:
                print()         # switch 마지막 값 출력하고 줄 바꿈
                return
        print()
        i += 1


N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())
for _ in range(student_num):
    S, num = map(int, sys.stdin.readline().split())
    if S == 1:      # 남학생
        i = 1
        idx = num
        while idx <= N:
            if switch[idx-1] == 1:
                switch[idx-1] = 0
            else:
                switch[idx-1] = 1
            i += 1
            idx = num * i

    else:           # 여학생
        i = 0
        while 0 <= num-1-i and num-1+i < N and switch[num-1-i] == switch[num-1+i]:
            if switch[num-1-i] == 1:
                switch[num - 1 - i] = switch[num - 1 + i] = 0
            else:
                switch[num - 1 - i] = switch[num - 1 + i] = 1
            i += 1

print_20(switch)