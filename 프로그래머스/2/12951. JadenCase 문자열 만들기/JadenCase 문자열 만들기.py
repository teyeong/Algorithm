import re

def solution(s):
    answer = ''
    list_s = re.findall(r'\S+|\s', s)
    for i in list_s:
        temp = list(i)
        for j in range(len(i)):
            if j == 0 and i[j].islower():
                temp[j] = i[j].upper()
            elif j > 0 and i[j].isupper():
                temp[j] = i[j].lower()
        answer += ''.join(temp)
    return answer