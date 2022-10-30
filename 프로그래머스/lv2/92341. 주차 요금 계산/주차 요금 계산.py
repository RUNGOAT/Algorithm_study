import math


def htom_time(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])


def cal_fee(total_time, bt, bp, ut, up):
    if total_time <= bt:
        return bp
    return bp + math.ceil((total_time - bt) / ut) * up


def solution(fees, records):
    answer = []
    #base_time, base_price, unit_time, unit_price
    bt, bp, ut, up = fees
    car_time = [-1] * 10000
    car_fee = [0] * 10000
    car_num = set()
    for record in records:
        t, n, in_out = record.split()
        n = int(n)
        if in_out == 'IN':
            car_time[n] = htom_time(t)
            car_num.add(n)
        else:
            car_fee[n] += htom_time(t) - car_time[n]
            car_time[n] = -1
    for n in car_num:
        if car_time[n] != -1:
            car_fee[n] += 1439 - car_time[n]
        car_fee[n] = cal_fee(car_fee[n], bt, bp, ut, up)

    car_num = sorted(list(car_num))
    for n in car_num:
        answer.append(car_fee[n])

    return answer
