def solution(today, terms, privacies):
    answer = []

    idx = 1
    for privacy in privacies:
        date, term = privacy.split()
        year, month, day = map(int, date.split("."))

        for tmp in terms:
            term_type, period = tmp.split()
            if term == term_type:
                month += int(period)
                day -= 1
                break

        date = get_date(f'{year}.{month}.{day}')
        if check(today, date):
            answer.append(idx)
        idx += 1
        
    return answer


def check(today, date):
    today = list(map(int, today.split(".")))
    year, month, day = map(int, date.split("."))
    
    if year < today[0]:
        return True
    elif year > today[0]:
        return False
    if month < today[1]:
        return True
    elif month > today[1]:
        return False
    if day >= today[2]:
        return False
    return True


def get_date(date):
    year, month, day = map(int, date.split("."))
    while month > 12:
        year += 1
        month -= 12

    if day == 0:
        month -= 1
        day = 28
        
    if month == 0:
        month = 12
        
    return f'{year}.{month}.{day}'