# def charge_cnt(n, k, charge):
#     cnt = 0
#     i = 0
#     while i < n-k:
#         for j in range(k, 0, -1):
#             if charge[i+j] == 1:
#                 cnt += 1
#                 i += j
#                 break
#         else:       # k번 안에 충전기(1)이 없으면 0
#             return 0
#     return cnt
#

T = int(input())

for t in range(1, T+1):
    k, n, m = map(int, input().split())
    charge_idx = list(map(int, input().split()))
    charge = [0] * (n+1)
    cnt = 0

    for i in range(m):
        charge[charge_idx[i]] = 1

    i = 0
    while i < n - k:      # 충전 후 반복문에 돌아오기 때문에 i의 최댓값은 마지막 충전 전까지
        for j in range(k, 0, -1):   # k 범위의 충전기 중 가장 오른쪽에서 충전
            if charge[i + j] == 1:
                cnt += 1
                i += j      # 충전한 위치부터 반복문 i값 설정
                break
        else:  # k 범위 안에 충전기(1)이 없으면 0
            cnt = 0
            break

    print(f'#{t} {cnt}')
