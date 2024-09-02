today = list(map(int, input().split()))
dday = list(map(int, input().split()))

ans = 0

# 윤년 계산
leap_year = []
for i in range(today[0], dday[0] + 1):
    if not i % 4:
        if i % 100:
            leap_year.append(i)
        elif not i % 400:
            leap_year.append(i)

# 연도 계산
ans += (dday[0] - today[0] + 1) * 365 + len(leap_year)

# 달 계산
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, today[1]):
    if today[0] in leap_year:
        if i == 2:
            ans -= 29
        else:
            ans -= month[i - 1]
    else:
        ans -= month[i - 1]

ans -= today[2]

for i in range(dday[1] + 1, 13):
    if dday[0] in leap_year:
        if i == 2:
            ans -= 29
        else:
            ans -= month[i - 1]
    else:
        ans -= month[i - 1]

if dday[0] in leap_year:
    if dday[1] == 2:
        ans -= 29 - dday[2]
    else:
        ans -= month[dday[1] - 1] - dday[2]
else:
    ans -= month[dday[1] - 1] - dday[2]

print(f'D-{ans}' if ans <= 365242 else 'gg')