import sys
input = sys.stdin.readline

s = list(input().rstrip())

start, end = 0, len(s) - 1
flag = 1
while start < end:
    if s[start] != s[end]:
        flag = 0
        break
    start += 1
    end -= 1
print(flag)