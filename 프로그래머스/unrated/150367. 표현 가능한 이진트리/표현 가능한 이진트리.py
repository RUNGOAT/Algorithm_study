def search(bin_number):
    length = len(bin_number)
    if length == 1 or '1' not in bin_number or '0' not in bin_number:
        return True
    
    mid = length // 2
    if bin_number[mid] == '0':
        return False
    
    return search(bin_number[:mid]) and search(bin_number[mid+1:])


def solution(numbers):
    answer = []
    bin_list = [2 ** i - 1 for i in range(50)]
    for number in numbers:
        bin_number = bin(number)[2:]
        length = len(bin_number)
        for num in bin_list:
            if num >= length:
                bin_number = '0' * (num - length) + bin_number
                break
        answer.append(1 if search(bin_number) else 0)
        
    return answer