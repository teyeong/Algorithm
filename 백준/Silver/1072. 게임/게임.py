X, Y = map(int, input().split())
Z = int(Y * 100 / X)
start, end = 0, 10**9 + X
flag = 0
while start <= end:
    mid = (start + end) // 2
    if int(((Y + mid) / (X + mid)) * 100) > Z:
        end = mid - 1
        flag = 1
    else:
        start = mid + 1

if flag:
    print(start)
else:
    print(-1)