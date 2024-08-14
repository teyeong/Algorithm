S = input().rstrip()
T = input().rstrip()

while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:len(T) - 1]
    else:
        T = T[:len(T) - 1]
        T = ''.join(reversed(T))

if S == T:
    print(1)
else:
    print(0)