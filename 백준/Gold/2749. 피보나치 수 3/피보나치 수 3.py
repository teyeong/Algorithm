import sys
input = sys.stdin.readline

N = int(input())

A = [[1, 1], [1, 0]]

def power(A, B):
    n = len(A)
    answer = [[0] * n for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            s = 0
            for a, b in zip(A[r], B[:]):
                s += a * b[c]
            answer[r][c] = s % 1000000
     
    return answer

def div_power(A, B):
    if B == 1:
        return A
    
    T = div_power(A, B // 2)
    if B % 2:
        return power(power(T, T), A)
    else:
        return power(T, T)

answer = div_power(A, N)

print(answer[0][1] % 1000000)