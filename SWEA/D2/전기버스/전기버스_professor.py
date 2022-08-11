def f(arr, k, n, m):
    arr = [0] + arr + [n]      # 출발점과 도착점 추가
    last = arr[0]              # 마지막 충전한 충전소 번호
    cnt = 0                    # 충전 횟수

    for i in range(1, len(arr)):
        # 충전기 사이가 K보다 크면 충전할 수 없음
        if arr[i] - arr[i - 1] > K:
            return 0
        # 충전할 수 없는 경우 앞 쪽에서 충전해야 함
        elif arr[i] > last + K:
            last = arr[i - 1]
            cnt += 1
    return cnt


T = int(input())

for t in range(1, T+1):
    # K : 한 번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점
    # M : 충전기가 설치된 갯수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))        # 충전기가 설치된 인덱스

    print(f'#{t} {f(charge, K, N, M)}')


    # last = charge[0]
    # cnt = 0
    # for i in range(1, len(charge)):
    #     if charge[i] - charge[i-1] > K:
    #         print(f'#{t} 0')
    #         break
    #     elif charge[i] > last + K:
    #         last = charge[i-1]
    #         cnt += 1
    # else:
    #     print(f'#{t} {cnt}')