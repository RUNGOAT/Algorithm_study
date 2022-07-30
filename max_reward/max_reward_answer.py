T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num, n = input().split()
    n = int(n)
    num_lst = [int(i) for i in list(num)]
    sort_num_lst = sorted(num_lst, reverse=True)

    for i in range(n):
        if num_lst == sort_num_lst:
            idx1, idx2 = 0, 0
            for l in range(len(num_lst)):
                if sort_num_lst.count(num_lst[l]) >= 2:
                    idx1 = l
                    for m in range(l, len(num_lst)):
                        if num_lst[l] == num_lst[m]:
                            idx2 = m
                            break
                    break
                else:
                    idx1 = -1
                    idx2 = -2
                    break
            num_lst[idx1], num_lst[idx2] = num_lst[idx2], num_lst[idx1]
        else:
            dif_num = []
            for k in range(len(num_lst)):
                if num_lst[k] != sort_num_lst[k]:
                    dif_num.append(k)
            chg = dif_num[0]

            if num_lst[chg] != sort_num_lst[chg]:
                for j in dif_num:
                    if num_lst[j] == sort_num_lst[chg]:
                        index = j
                        break
                num_lst[chg], num_lst[index] = num_lst[index], num_lst[chg]

    num_lst = ''.join([str(chr_num) for chr_num in num_lst])
    print(f'#{test_case} {num_lst}')