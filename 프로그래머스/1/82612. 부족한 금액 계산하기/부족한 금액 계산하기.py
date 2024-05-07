def solution(price, money, count):
    answer = 0
    
    for i in range(count):
        answer += price * (i + 1)
        
    if answer > money:
        answer -= money
    else:
        answer = 0

    return answer 