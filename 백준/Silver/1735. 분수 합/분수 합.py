import math

def fraction_sum(a, b, c, d):
    denominator = b * d
    numerator = (a * d) + (c * b)
    
    gcd = math.gcd(denominator, numerator)
    
    denominator //= gcd
    numerator //= gcd
    
    return numerator, denominator

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator, denominator = fraction_sum(a, b, c, d)
print(numerator, denominator)