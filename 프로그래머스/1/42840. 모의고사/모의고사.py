def solution(answers):
    answer = []
    
    # 수포자별 답안
    people = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 정답 개수 계산 dict
    score = {}
    
    for idx, person in enumerate(people):
        person_idx = 0
        total = 0
        
        # 정답과 답안이 일치하는 개수 계산
        for val in answers:
            if person[person_idx] == val:
                total += 1
            person_idx = (person_idx + 1) % len(person)
            
        score[idx] = total
    
    # 가장 많은 개수 계산
    max_score = max(val for val in score.values())

    # max_score와 일치하면 answer에 추가
    for key, score in score.items():
        if max_score == score:
            answer.append(key + 1)
    
    # 정렬하여 반환
    return sorted(answer)