from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    total_element = len(queue1) * 3
    while q1_sum != q2_sum and answer < total_element:
        answer += 1
        if q1_sum > q2_sum:
            element = queue1.popleft()
            queue2.append(element)
            q1_sum -= element
            q2_sum += element
        else:
            element = queue2.popleft()
            queue1.append(element)
            q2_sum -= element
            q1_sum += element
    if answer == total_element:
        answer = -1
        
    return answer