import sys
N = int(sys.stdin.readline())
meeting_time = []
for _ in range(N):
    meeting_time.append(list(map(int, sys.stdin.readline().split())))
meeting_time.sort(key=lambda x: (x[1], x[0]))

tmp = [meeting_time[0]]
for i in range(1, N):
    if tmp[-1][1] <= meeting_time[i][0]:
        tmp.append(meeting_time[i])

print(len(tmp))
