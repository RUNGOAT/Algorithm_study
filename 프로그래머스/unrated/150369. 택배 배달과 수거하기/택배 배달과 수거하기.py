def solution(cap, n, deliveries, pickups):
    answer = 0

    def move(arr):
        while arr and arr[-1] == 0:
            arr.pop()
        distance = len(arr)
        box = cap
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != 0:
                if arr[i] <= box:
                    box -= arr[i]
                    arr[i] = 0
                else:
                    arr[i] -= box
                    break
        return distance

    while True:
        go_dist = move(deliveries)
        back_dist = move(pickups)
        if go_dist == 0 and back_dist == 0:
            break
        answer += max(go_dist, back_dist) * 2

    return answer