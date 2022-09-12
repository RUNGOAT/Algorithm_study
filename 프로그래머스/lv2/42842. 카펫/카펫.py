import math

def solution(brown, yellow):
    arr_cnt = brown + yellow
    column = int(math.sqrt(yellow))
    
    while True:
        if ((yellow // column) + 2) * (column + 2) == arr_cnt:
            break
        else:
            column -= 1
        
    row = yellow // column
    return [row+2, column+2]
