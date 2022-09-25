# 0번은 인덱스 조절용
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
 
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    gunjib = dict()
    for k in range(K):
        x, y, bug, d = map(int, input().split())
        gunjib[(x, y)] = [[bug, d]]
 
    for m in range(M):
        tmp = []
        for k, v in gunjib.items():
            x, y = k
            bug, d = v[0]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 < nx < N-1 and 0 < ny < N-1:
                tmp.append([nx, ny, bug, d])
            else:
                gunjib[k][0][0] //= 2
                if d == 1:
                    gunjib[k][0][1] = 2
                elif d == 2:
                    gunjib[k][0][1] = 1
                elif d == 3:
                    gunjib[k][0][1] = 4
                else:
                    gunjib[k][0][1] = 3
                tmp.append([nx, ny, gunjib[k][0][0], gunjib[k][0][1]])
 
        dic = dict()
        for t in tmp:
            if (t[0], t[1]) in dic:
                dic[(t[0], t[1])] += [[t[2], t[3]]]
            else:
                dic[(t[0], t[1])] = [[t[2], t[3]]]
 
        for k, v in dic.items():
            if len(v) > 1:
                dic[k] = [[sum([x[0] for x in v]), max(v)[1]]]
 
        gunjib = dic
 
    ans = 0
    for v in gunjib.values():
        ans += v[0][0]
    print(f'#{tc} {ans}')