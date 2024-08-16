import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def func(T):
    if len(S) == len(T):
        return S == T
    if T[-1] == 'A' and func(T[:-1]):
        return 1
    if T[0] == 'B' and func(T[:0:-1]):
        return 1

print(1 if func(T) else 0)