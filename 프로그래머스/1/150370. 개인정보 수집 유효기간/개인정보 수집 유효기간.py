import re

def solution(today, terms, privacies):
    answer = []
    terms_alpha = []
    terms_dura = []
    today_list = list(map(int, re.split('[.]', today)))
    
    for j in range(len(terms)):
        alphabet, duration = re.split('[ ]', terms[j])
        terms_alpha.append(alphabet)
        terms_dura.append(int(duration))
    
    for i in range(len(privacies)):
        Y, M, D, term = re.split('[ .]', privacies[i])
        term_index = terms_alpha.index(term)
        
        plus_year = 0
        plus_month = terms_dura[term_index]
        if (plus_month > 11):
            plus_year = plus_month // 12
            plus_month %= 12
        
        result_year = int(Y) + plus_year
        result_month = int(M) + plus_month
        result_day = int(D)
        
        if (result_month > 12):
            result_year += 1
            result_month -= 12
        
        if (result_year < today_list[0]):
            answer.append(i + 1)
            continue
        
        if (result_year == today_list[0]):
            if (result_month < today_list[1]):
                answer.append(i + 1)
            elif (result_month == today_list[1]):
                if (result_day <= today_list[2]):
                    answer.append(i + 1)
    return answer