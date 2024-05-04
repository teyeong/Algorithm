def solution(n):
    x = 1
    
    while n > x:
        if (n % x == 1):
            break
        x += 1
    
    return x