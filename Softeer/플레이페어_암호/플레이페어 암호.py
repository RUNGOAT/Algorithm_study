import sys
input = sys.stdin.readline


def check(x1, y1, x2, y2):
    if x1 == x2:
        y1 = (y1+1) % 5
        y2 = (y2+1) % 5
    elif y1 == y2:
        x1 = (x1+1) % 5
        x2 = (x2+1) % 5
    else:
        y1, y2 = y2, y1
    return x1, y1, x2, y2


message = input().strip()
key = input().strip()

visited = [False] * 26
visited[9] = True   # J값 처리
arr = [[''] * 5 for _ in range(5)]

# 중복 제거한 key
set_key = []
for s in key:
    if not visited[ord(s) - 65]:
        set_key.append(s)
        visited[ord(s) - 65] = True

# 사용되지 않은 문자
no_use_str = []
for n in range(26):
    if not visited[n]:
        no_use_str.append(chr(n + 65))

# 5*5 표 생성
n = 0
flag = True
tmp = set_key
for i in range(5):
    for j in range(5):
        if flag and n == len(set_key):
            n = 0
            tmp = no_use_str
            flag = False
        arr[i][j] = tmp[n]
        n += 1

# 두 글자 암호화
secret_list = []
tmp = message[0]
i = 1
while i < len(message):
    if tmp:
        if message[i] == tmp:
            if tmp == 'X':
                tmp += 'Q'
            else:
                tmp += 'X'
            i -= 1
        else:
            tmp += message[i]
        secret_list.append(tmp)
        tmp = ''
    else:
        tmp = message[i]
    i += 1
if tmp:
    tmp += 'X'
    secret_list.append(tmp)

# 암호화 결과
secret_result = ''

dic = {}
for i in range(5):
    for j in range(5):
        dic[arr[i][j]] = (i, j)

for a, b in secret_list:
    ax, ay = dic[a]
    bx, by = dic[b]
    x1, y1, x2, y2 = check(ax, ay, bx, by)
    secret_result += arr[x1][y1] + arr[x2][y2]

print(secret_result)
