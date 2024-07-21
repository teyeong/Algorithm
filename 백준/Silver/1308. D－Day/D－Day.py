from datetime import datetime

today = list(map(int, input().split()))
dday = list(map(int, input().split()))

limit_day = datetime(today[0] + 1000, today[1], today[2])
today = datetime(today[0], today[1], today[2])
dday = datetime(dday[0], dday[1], dday[2])

diff = dday - today

if diff >= limit_day - today:
    print("gg")
else:
    print(f"D-{diff.days}")