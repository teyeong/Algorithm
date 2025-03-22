from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    return ''.join(numbers) if numbers[0] != '0' else '0'

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1