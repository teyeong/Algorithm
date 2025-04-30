import itertools

def solution(word):
    dictionary = []
    for i in range(1, 6):
        pro = itertools.product('AEIOU', repeat=i)
        for val in list(pro):
            dictionary.append(''.join(val))
    
    dictionary.sort()
    return dictionary.index(word) + 1