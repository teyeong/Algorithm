import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = list(input().rstrip())

def check_left(i):
    for j in range(i - K, i):
        if 0 <= j < N and s[j] == 'H':
            s[j] = 0
            return
    return check_right(i)

def check_right(i):
    for j in range(i + 1, i + K + 1):
        if 0 <= j < N and s[j] == 'H':
            s[j] = 0
            return
    return

for i in range(N):
    if s[i] == 'P':
        check_left(i)
print("".join(map(str, s)).count('0'))