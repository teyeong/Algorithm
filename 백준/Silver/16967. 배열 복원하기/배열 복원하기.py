import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H + X)]
A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i < X or j < Y:
            # A에만 포함
            A[i][j] = B[i][j]
        elif i >= X or j >= Y:
            # A와 B 겹치는 부분
            A[i][j] = B[i][j] - A[i - X][j - Y]
                
for i in range(H):
    for j in range(W):
        print(A[i][j], end=' ')
    print()