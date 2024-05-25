def solution(brown, yellow):
    sum = (brown + 4) // 2
    mul = brown + yellow
    
    for y in range(1, mul + 1):
        if (mul / y) % 1 == 0:
            x = mul // y;
            if x >= y:
                if sum == x + y:
                    return [x, y]
        
    return []