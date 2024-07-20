def is_promising(x):
    for i in range(x):
        # 1. 같은 열에 다른 퀸이 있는 경우
        # 2. 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queen(x):
    global cnt
    
    if x == N:
        cnt += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queen(x + 1)

N = int(input())

cnt = 0
row = [0] * N

n_queen(0)
print(cnt)