import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
def is_palindrome(x):
    left, right = 0, 0
    length = len(x)
    if length % 2 == 0:
        left, right = length // 2 - 1, length // 2
    else:
        left, right = length // 2 - 1, length // 2 + 1
    
    while left >= 0 and right < length:
        if x[left] == x[right]:
            left -= 1
            right += 1
        else:
            return False
    return True

N = int(input())

while True:
    if is_prime(N) and is_palindrome(list(str(N))):
        print(N)
        break
    else:
        N += 1