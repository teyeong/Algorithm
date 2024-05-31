def combination(n, m):
    numerator = 1
    denominator1 = 1
    denominator2 = 1
    for i in range(1, n + 1):
        numerator *= i
    for j in range(1, m + 1):
        denominator1 *= j
    for t in range(1, n - m + 1):
        denominator2 *= t
        
    return int(numerator // (denominator1 * denominator2))

n, m = map(int, input().split())
print(combination(n, m))