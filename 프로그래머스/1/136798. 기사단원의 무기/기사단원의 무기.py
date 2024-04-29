def divisor(number):
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number // i:
                result.append(number//i)
    return len(result)

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        weapon = divisor(i)
        if weapon > limit:
            weapon = power
        answer += weapon
        
    return answer