N, r, c = map(int, input().split())

def z(n, row, col):
    if n == 0:
        return 0
    curr_cnt = 2 * (row % 2) + (col % 2)
    return 4 * z(n - 1, row // 2, col // 2) + curr_cnt

print(z(N, r, c))