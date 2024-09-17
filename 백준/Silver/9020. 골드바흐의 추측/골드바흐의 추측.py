import sys
import math
input = sys.stdin.readline

T = int(input())

chk = [True] * (10001)
primes = []
chk[0], chk[1] = False, False

for i in range(2, int(math.sqrt(10000))+1):
    if chk[i]:
        primes.append(i)
        j = 2
        while i * j <= 10000:
            chk[i * j] = False
            j += 1
primes = [x for x in range(10001) if chk[x]]

for _ in range(T):
    n = int(input())
    a, b = n // 2, n // 2
    while a > 0:
        if a in primes and b in primes:
            print(a, b)
            break
        else:
            a -= 1
            b += 1