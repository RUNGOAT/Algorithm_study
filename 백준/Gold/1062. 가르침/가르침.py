import sys
input = sys.stdin.readline


def check():
    cnt = 0
    for word in words:
        flag = True
        for s in word:
            if not visited[ord(s) - 97]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt


def dfs(idx, cnt):
    global ans
    if cnt == K:
        ans = max(ans, check())
        return
    for i in range(idx, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


N, K = map(int, input().split())
K -= 5
words = [set(input().rstrip()) for _ in range(N)]

visited = [False] * 26
visited[ord('a') - 97] = True
visited[ord('n') - 97] = True
visited[ord('t') - 97] = True
visited[ord('i') - 97] = True
visited[ord('c') - 97] = True

if K < 0:
    print(0)
    exit(0)
if K == 21:
    print(N)
    exit(0)

ans = 0
dfs(0, 0)
print(ans)
