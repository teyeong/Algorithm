def solution(s):
    list_s = []
    
    for i in s:
        list_s.append(i)
        if len(list_s) > 1 and list_s[-2] == list_s[-1]:
            list_s.pop()
            list_s.pop()
    
    if list_s:
        return 0
    else:
        return 1