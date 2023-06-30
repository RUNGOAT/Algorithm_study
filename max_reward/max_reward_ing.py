T = int(input())
for t in range(1, T + 1):
    lst, N = map(str, input().split())
    lst1 = list(lst)
    lst2 = sorted(lst1, reverse=True)

    if lst1 == lst2:
        for n in range(int(N)):
            if lst1.count(lst1[n]) > 1:
                lst_dupli = [i for i, value in enumerate(lst1) if value == lst1[n]]
                idx1 = lst_dupli[0]
                idx2 = lst_dupli[1]
                lst1[idx1], lst1[idx2] = lst1[idx2], lst1[idx1]
            else:    
                lst1[-2], lst1[-1] = lst1[-1], lst1[-2]
    else:
        result = 0
        for i in range(len(lst)):
            if lst1[i] != lst2[i]:
                lst3 = lst1[:]
                lst3.reverse()
                high_index = lst3.index(lst2[i])
                lst1[len(lst1)-1-high_index], lst1[i] = lst1[i], lst1[len(lst1)-1-high_index]
                result += 1
                if result == int(N):
                    break

        if result < int(N):
            if lst1.count(lst1[n]) > 1:
                lst_dupli = [i for i, value in enumerate(lst1) if value == lst1[n]]
                idx1 = lst_dupli[0]
                idx2 = lst_dupli[1]
                lst1[idx1], lst1[idx2] = lst1[idx2], lst1[idx1]
            else:    
                lst1[-2], lst1[-1] = lst1[-1], lst1[-2]

    print(f'#{t} {''.join(lst1)}')
    
