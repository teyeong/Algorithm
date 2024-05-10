def solution(s):
    answer = ''
    
    new_s = list(map(int, s.split()))
    new_s.sort()
    answer = str(new_s[0]) + ' ' + str(new_s[-1])
    
    return answer