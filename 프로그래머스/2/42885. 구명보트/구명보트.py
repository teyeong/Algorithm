def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            i += 1
    
    return answer