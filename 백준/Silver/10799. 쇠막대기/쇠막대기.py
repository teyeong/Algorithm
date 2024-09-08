import sys
input = sys.stdin.readline

exp = input().rstrip()
cnt = 0
res = 0

new_exp = exp.replace('()', '*')

for ch in new_exp:
    if ch == '(':
        cnt += 1
    elif ch == ')':
        cnt -= 1
        res += 1
    else:
        res += cnt
print(res)