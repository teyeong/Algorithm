T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    sum_r = (r1 + r2) ** 2
    sub_r = (r1 - r2) ** 2
    
    if r1 == r2 and x1 == x2 and y1 == y2:
        print(-1)
    elif d > sub_r and d < sum_r:
        print(2)
    elif d == sum_r or d == sub_r:
        print(1)
    elif d > sum_r or d < sub_r:
        print(0)