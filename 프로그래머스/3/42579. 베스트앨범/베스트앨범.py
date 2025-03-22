def solution(genres, plays):
    answer = []
    
    best = {}           # 장르별 노래 dict
    best_genres = {}    # 장르 총 재생수 dict
    
    for i in range(len(genres)):
        content = [plays[i], i]
        if genres[i] not in best.keys():
            best[genres[i]] = [content]
            best_genres[genres[i]] = plays[i]
        else:
            best[genres[i]].append(content)
            best_genres[genres[i]] += plays[i]
    
    # 재생수 높은순 장르 정렬
    sorted_genres = sorted(best_genres, key=lambda x: best_genres[x], reverse=True)
    
    for i in range(len(sorted_genres)):
        # 장르당 [재생횟수, 고유번호] 리스트
        curr = best.pop(sorted_genres[i])
        # 재생횟수 내림차순, 고유번호 오름차순 정렬
        curr.sort(key=lambda x: (-x[0], x[1]))
        
        # 장르 별로 가장 많이 재생된 노래 2개씩 모으기
        for _, song_id in curr[:2]:
            answer.append(song_id)
    
    return answer