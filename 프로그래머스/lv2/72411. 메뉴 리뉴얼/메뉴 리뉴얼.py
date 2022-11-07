from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for cnt in course:
        total_menu = []
        for order in orders:
            order = sorted(order)
            total_menu.extend(list(combinations(order, cnt)))
        total_menu = Counter(total_menu)
        if len(total_menu) != 0 and max(total_menu.values()) != 1:
            max_v = max(total_menu.values())
            for menu in total_menu:
                if total_menu[menu] == max_v:
                    answer.append(''.join(menu))

    return sorted(answer)
