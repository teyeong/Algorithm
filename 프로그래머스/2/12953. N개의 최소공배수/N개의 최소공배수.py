import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    answer = 1
    result = 1
    
    for i in range(len(arr) - 1):
        print(arr[i] + arr[i + 1])
        result = lcm(arr[i], arr[i + 1])
        answer = lcm(result, answer)
    
    return answer