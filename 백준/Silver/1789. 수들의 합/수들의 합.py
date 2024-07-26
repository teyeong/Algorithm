S = int(input())

cnt = num = 0

while S > num:
    cnt += 1
    num += cnt
    if S == num:
        cnt += 1
        break

print(cnt - 1)