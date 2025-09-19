def solution(storey):
    answer = 0
    
    length = len(str(storey))
    i = 0
    while i < length:
        i += 1
        quotient = storey // 10 % 10
        remainder = storey % 10
        storey //= 10
        if remainder > 5:
            storey += 1
            answer += 10 - remainder
        elif remainder < 5:
            answer += remainder
        else:
            if quotient >= 5:
                storey += 1
                answer += 10 - remainder
            else:
                answer += remainder
    
    if storey > 0:
        answer += storey
    
    return answer