import sys
input = sys.stdin.readline

name = input().rstrip()
big_letters = [0] * 26
for ch in name:
    big_letters[ord(ch) - 65] += 1

front = back = mid = res = ""
flag = 0
for i in range(26):
    if not big_letters[i] % 2: # 짝수
        for j in range(big_letters[i] // 2):
            front = front + chr(i + 65)
            back = chr(i + 65) + back
    else: # 홀수
        if flag:
            res = "I'm Sorry Hansoo"
            break
        else:
            flag = 1
            mid = chr(i + 65)
            for j in range(big_letters[i] // 2):
                front = front + chr(i + 65)
                back = chr(i + 65) + back
if res:
    print(res)
else:
    print(front + mid + back)