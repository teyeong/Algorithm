import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())

while True:
    if is_prime(N) and str(N) == str(N)[::-1]:
        print(N)
        break
    else:
        N += 1