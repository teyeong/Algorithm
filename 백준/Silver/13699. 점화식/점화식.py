import sys
input = sys.stdin.readline

n = int(input())

t = [0] * 36
t[0] = 1
t[1] = 1
t[2] = 2

for i in range(3, n + 1):
    for j in range(i):
        t[i] += (t[j] * t[i - j - 1])
print(t[n])