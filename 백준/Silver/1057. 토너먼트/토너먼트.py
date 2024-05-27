def tournament(N, jimin, hansu):
    rnd = 1
    
    while N > 0:
        if jimin > hansu:
            later = jimin
        else:
            later = hansu
            
        if abs(jimin - hansu) == 1 and later % 2 == 0:
            break
        
        jimin = (jimin + 1) // 2
        hansu = (hansu + 1) // 2
        N //= 2
        rnd += 1
        
    return rnd

N, jimin, hansu = input().split()

N = int(N)
jimin = int(jimin)
hansu = int(hansu)

print(tournament(N, jimin, hansu))